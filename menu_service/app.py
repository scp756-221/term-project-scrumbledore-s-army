from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hga50:12345678@restaurant-db.cj7sflyjpv0c.us-west-2.rds.amazonaws.com:5432/restaurant_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'


class Menu(db.Model):
    _tablename_ = 'menu'
    m_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def _init_(self, pname, color):
        self.name = pname
        self.price = color




@app.route('/getMenuItems')
def get_all_menu_data():
    menu_items = Menu.query.all()
    results = [
        {
            "mid": m.m_id,
            "name": m.name,
            "price": m.price
        } for m in menu_items]
    return {"menu_items": results}




class Order(db.Model):
    _tablename_ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=True)
    amount = db.Column(db.Integer, nullable=True)
    paid = db.Column(db.Boolean, nullable=True)

    def _init_(self, user_id, amount, paid):
        self.user_id = user_id
        self.amount = amount
        self.paid = paid





@app.route('/takeOrder', methods=['POST'])
def take_order():

    order = json.loads(request.data)
    user_id = order['user_id']
    order_list = order['order_list']    
    
    total_price=0
    for order_obj in order_list:
        # {
        #     "id": 1,
        #     "name": "aa",
        #     "price": 12.0,
        #     "qty": 1
        # },
        price = order_obj['price']
        qty = order_obj['qty']
        total_price += (price * qty)
    # print(order)

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
    db.create_all()
    app.run(debug=True)
