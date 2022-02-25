import argparse
import json

from flask import Flask, jsonify, make_response, request

import db.dynamodb_handler as dynamodb

app = Flask(__name__)


def parse_args():
    argp = argparse.ArgumentParser('Menu-service')
    argp.add_argument('port_menu', type=int, help="Port number of menu server")

    return argp.parse_args()


@app.route('/getMenuItems')
def get_all_menu_data():
    return dynamodb.get_menu()


@app.route('/takeOrder', methods=['POST'])
def take_order():
    menu_data = dynamodb.get_menu()
    order = json.loads(json.loads(request.data))
    user_id = order['user_id']
    order_list = order['order_list']

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

    return dynamodb.add_order(user_id, total_price, False)


if __name__ == '__main__':
    args = parse_args()
    app.run(host='0.0.0.0', port=args.port_menu, debug=True)
