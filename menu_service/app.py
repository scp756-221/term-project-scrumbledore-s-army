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

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
