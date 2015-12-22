from flask import Blueprint, render_template

app = Blueprint('payment', __name__, template_folder='templates')


@app.route('/customer')
def customer_payment():
    return render_template('customer.html')


@app.route('/contributor')
def contributor_payment():
    return "contributor payment page "
