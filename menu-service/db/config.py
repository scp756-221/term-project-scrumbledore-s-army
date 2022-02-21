from flask import Flask

SQLALCHEMY_DATABASE_URI = 'postgresql://hga50:12345678@restaurant-db.cj7sflyjpv0c.us-west-2.rds.amazonaws.com:5432/restaurant_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
