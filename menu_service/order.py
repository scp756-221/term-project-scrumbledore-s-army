from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json


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