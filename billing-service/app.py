from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hga50:12345678@restaurant-db.cj7sflyjpv0c.us-west-2.rds.amazonaws.com:5432/restaurant_db'
db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    amount = db.Column(db.Integer)
    paid = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.user_id

@app.route('/bill', methods=['GET'])
def generate_bill():
    user = request.args.get('user_id')
    order = get_user_data(user)

    return make_response(order, 200)
    
  
@app.route('/pay', methods=['GET'])
def make_payment():
    user = request.args.get('user_id')
    data = Order.query.filter_by(user_id=user).update({Order.paid: True})
    db.session.commit()
    order = get_user_data(user)

    return make_response(order, 200)

def get_user_data(user):
    data = Order.query.filter_by(user_id=user).first()
    order = {
        "user_id":data.user_id,
        "amount":data.amount,
        "paid":data.paid
    }

    return order

if __name__ == '__main__':
    app.run(port=5000, debug=True)
