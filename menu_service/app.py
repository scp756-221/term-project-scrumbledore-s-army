from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
from menu import Menu 
from order import Order   
from db.config import app
import argparse

db = SQLAlchemy(app)

def parse_args():
    argp = argparse.ArgumentParser(
        'Menu-service'
        )
    argp.add_argument(
        'port_menu',
        type=int,
        help="Port number of menu server"
        )

    return argp.parse_args()

@app.route('/getMenuItems')
def get_all_menu_data():
    return get_menu_data()


def get_menu_data():
    menu_items = Menu.query.all()
    results = [
        {
            "mid": m.m_id,
            "name": m.name,
            "price": m.price
        } for m in menu_items]
    return {"menu_items": results}

@app.route('/takeOrder', methods=['POST'])
def take_order():
    res_data = get_menu_data()
    order = json.loads(request.data)
    user_id = order['user_id']
    order_list = order['order_list']    
    
    total_price=0
    for selected_o in order_list:
        for res_o in res_data["menu_items"]:
            if int(selected_o['id']) == int(res_o['mid']):
                qty = selected_o['qty']
                price = res_o['price']
                total_price += (price * qty)

    _order_db = Order(user_id = user_id,
                    amount = total_price,
                    paid = False)

    db.session.add(_order_db)   
    db.session.commit()

    order_success = {
        "status": True,
        "message": "Order accepted",
        "total_amount": total_price
    }
    return jsonify(order_success)

if __name__ == '__main__':
    args = parse_args()
    app.run(port=args.port_menu, debug=True)
    
