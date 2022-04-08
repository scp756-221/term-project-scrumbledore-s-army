import argparse

import db.dynamodb_handler as dynamodb
from flask import Flask, make_response, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Billing Service')


def parse_args():
    argp = argparse.ArgumentParser('Billing-service')
    argp.add_argument('port_bill',
                      type=int,
                      help="Port number of billing server")

    return argp.parse_args()


@app.route('/bill', methods=['GET'])
def generate_bill():
    user = request.args.get('user_id')
    response = dynamodb.get_user_data(user)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Item' in response):
            return make_response(response["Item"], 200)

        return create_user_error()

    return create_user_error()


@app.route('/pay', methods=['GET'])
def make_payment():
    user = request.args.get('user_id')
    has_booking = 'booking_id' in request.args.keys()

    response = dynamodb.get_booking_data()
    table_id = None

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if has_booking:
            booking_id = request.args.get('booking_id')
            for table in response['Items']:
                if table['available'] == False and table[
                        'booking_id'] == booking_id:
                    table_id = table['table_id']
        else:
            for table in response['Items']:
                if table['available'] == False and table['booking_id'] is None:
                    table_id = table['table_id']

    table_response = dynamodb.set_table_availability(table_id)

    if table_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = dynamodb.get_user_data(user)

        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Item' in response):
                data = response['Item']

                if data["amount"] == 0:
                    return make_response(
                        "The amount value is zero. Cannot pay the bill.", 422)
                elif data["paid"] == True:
                    return make_response("The bill has already been paid.",
                                         409)

                else:
                    update_response = dynamodb.pay_bill(user)
                    if (update_response['ResponseMetadata']['HTTPStatusCode']
                            == 200):
                        return {
                            'msg': 'Paid successfully',
                            'ModifiedAttributes':
                            update_response['Attributes'],
                            'response': update_response['ResponseMetadata']
                        }

                    return {
                        'msg': 'Some error occured',
                        'response': update_response
                    }

            return create_user_error()

    return create_user_error()


def create_user_error():
    return make_response("Invalid user.", 422)


if __name__ == '__main__':
    args = parse_args()
    app.run(host='0.0.0.0', port=args.port_bill, debug=True)
