from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json

class Menu(db.Model):
    _tablename_ = 'menu'
    m_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def _init_(self, pname, color):
        self.name = pname
        self.price = color

