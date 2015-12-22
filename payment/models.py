from datetime import  date
from database import db

class Payment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    balance = db.Column(db.Float)
    credit = db.Column(db.Float)
    debit = db.Column(db.Float)
    create_date = db.Column(db.DateTime)

    def __init__(self, user_id, balance, credit, debit, create_date=date.today() ):
        self.user_id = user_id
        self.balance = balance
        self.credit = credit
        self.debit = debit
        self.create_date = create_date

