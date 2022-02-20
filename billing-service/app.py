from flask import make_response, request
from Order import Order
from db.config import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
import argparse

db = SQLAlchemy(app)

def parse_args():
    argp = argparse.ArgumentParser(
        'Billing-service'
        )
    argp.add_argument(
        'port_bill',
        type=int,
        help="Port number of billing server"
        )

    return argp.parse_args()

@app.route('/bill', methods=['GET'])
def generate_bill():
    user = request.args.get('user_id')
    order = get_user_data(user)
    if order == None:
        return create_user_error()
    else:
        return make_response(order, 200)
        
@app.route('/pay', methods=['GET'])
def make_payment():
    user = request.args.get('user_id')
    data = Order.query.filter_by(user_id=user).first()
    
    if data == None:
        return create_user_error()
    
    if data.amount == 0:
        return make_response("The amount value is zero. Cannot pay the bill.", 422)
    elif data.paid == True:
        return make_response("The bill has already been paid.", 409)
    else:
        data = Order.query.filter_by(user_id=user).first()
        data.paid = True
        Order.db.session.commit()
        order = get_user_data(user)
        if order == None:
            return create_user_error()
        else:
            return make_response(order, 200)

def get_user_data(user):
    data = Order.query.filter_by(user_id=user).first()
    if data == None:
        return None
    order = {
        "user_id":data.user_id,
        "amount":data.amount,
        "paid":data.paid
    }

    return order

def create_user_error():
    return make_response("Invalid user.", 422)
    
if __name__ == '__main__':
    args = parse_args()
    app.run(port=args.port_bill, debug=True)
    