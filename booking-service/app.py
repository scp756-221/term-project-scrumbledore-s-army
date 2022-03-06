import argparse

from flask import Flask, make_response, request

import db.dynamodb_handler as dynamodb

app = Flask(__name__)


def parse_args():
    argp = argparse.ArgumentParser('Booking-service')
    argp.add_argument('port_book',
                      type=int,
                      help="Port number of booking server")

    return argp.parse_args()


@app.route('/book', methods=['GET'])
def book_table():
    booking_data = dynamodb.get_booking_data()

    # if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
    #     if ('Item' in response):
    #         data = response['Item']

    #         if data["amount"] == 0:
    #             return make_response(
    #                 "The amount value is zero. Cannot pay the bill.", 422)
    #         elif data["paid"] == True:
    #             return make_response("The bill has already been paid.", 409)

    #         else:
    #             update_response = dynamodb.pay_bill(user)
    #             if (update_response['ResponseMetadata']['HTTPStatusCode'] ==
    #                     200):
    #                 return {
    #                     'msg': 'Paid successfully',
    #                     'ModifiedAttributes': update_response['Attributes'],
    #                     'response': update_response['ResponseMetadata']
    #                 }

    #             return {
    #                 'msg': 'Some error occured',
    #                 'response': update_response
    #             }



    # user = request.args.get('user_id')
    # response = dynamodb.get_user_data(user)

    # if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
    #     if ('Item' in response):
    #         return make_response(response["Item"], 200)

    #     return create_user_error()

    # return create_user_error()
    pass


@app.route('/get_booking', methods=['GET'])
def get_booking():
    booking_id = request.args.get('booking_id')
    response = dynamodb.get_booking_data(booking_id)
    if (response['ResponseMetadata']['HTTPStatusCode']==200):
        return make_response("success",200)
    else :
        return make_response("booking Id not found",response['ResponseMetadata']['HTTPStatusCode'])


if __name__ == '__main__':
    args = parse_args()
    app.run(host='0.0.0.0', port=args.port_book, debug=True)
