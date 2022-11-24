from base import db 


class LastSeen(db.Model): 
    user_id = db.Column(db.Integer(), primary_key=True) 
    user_name = db.Column(db.String(30), null=False) 
    status = db.Column(db.String())