from app.extensions import db
from datetime import datetime

class Company(db.Model):
        company_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(20), nullable = False)
        origin = db.Column(db.String(), nullable = False)
        description = db.Column(db.String(20), nullable = False)
        email =  db.Column(db.String(30), nullable = False, unique = True)
        contact = db.Column(db.String(10), nullable = False, unique = True)
        created_at = db.Column(db.DateTime, default = datetime.now())
        updated_at = db.Column(db.DateTime, onupdate = datetime.now())

        def __init__(self , company_id, name, origin, description , email, contact, created_at, updated_at ):
         self.company_id = company_id
         self.name = name
         self.origin = origin
         self.description = description
         self.email = email
         self.contact = contact
         self.created_at = created_at
         self.updated_at = updated_at
         
