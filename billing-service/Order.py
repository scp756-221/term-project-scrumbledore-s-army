from flask_sqlalchemy import SQLAlchemy
from db.config import app

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text)
    amount = db.Column(db.Integer)
    paid = db.Column(db.Boolean)

    db = db

    def __repr__(self):
        return '<User %r>' % self.user_id 
