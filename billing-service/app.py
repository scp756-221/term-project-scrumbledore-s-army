from flask import Flask

app = Flask(__name__)

@app.route('/bill')
def generate_bill():
    amt = 0
    return amt
    
  
@app.route('/pay')
def make_payment():
    return 'Payment Done'