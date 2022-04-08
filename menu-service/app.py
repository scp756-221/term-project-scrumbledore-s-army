import argparse
import json

import db.dynamodb_handler as dynamodb
from flask import Flask, jsonify, make_response, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Menu Service')


def parse_args():
    argp = argparse.ArgumentParser('Menu-service')
    argp.add_argument('port_menu', type=int, help="Port number of menu server")

    return argp.parse_args()


def place_order(order_list, user_id):
    menu_data = dynamodb.get_menu()
    total_price = 0

    for selected_o in order_list:
        item_found = False
        for res_o in menu_data["menu_items"]:
            if int(selected_o['id']) == int(res_o['m_id']):
                item_found = True
                qty = selected_o['qty']
                price = res_o['price']
                total_price += (price * qty)

        if item_found == False:
            order_failure = {"status": False, "message": "Order Declined"}

            return make_response(jsonify(order_failure), 422)

    response = dynamodb.add_order(user_id, total_price, False)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return make_response("Order successfully placed!", 200)

    return create_error(code=500)


@app.route('/getMenuItems')
def get_all_menu_data():
    return dynamodb.get_menu()


@app.route('/takeOrder', methods=['POST'])
def take_order():
    order = json.loads(json.loads(request.data))
    user_id = order['user_id']
    order_list = order['order_list']
    has_booked = order['has_booked']

    if not has_booked:
        seating = dynamodb.get_booking_data()
        if (seating['ResponseMetadata']['HTTPStatusCode'] == 200):
            for table_data in seating['Items']:
                if table_data['available']:
                    available_table_id = table_data['table_id']
                    dynamodb.book_table(available_table_id)

                    return place_order(order_list, user_id)
    else:
        return place_order(order_list, user_id)

    return create_error(code=500)


def create_error(code=422):
    return make_response("Invalid user.", code)


if __name__ == '__main__':
    args = parse_args()
    app.run(host='0.0.0.0', port=args.port_menu, debug=True)
