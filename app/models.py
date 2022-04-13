from tkinter import E
import unicodedata
from . import db


class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True) 
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.Integer, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    number_of_guests = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.String(250), nullable=False)

    def __init__(self, id, firstname, lastname, phonenumber, date, number_of_guests, email, address, equipment_needed):
        self.id = id
        self.firstname = firstname 
        self.lastname = lastname 
        self.phonenumber = phonenumber
        self.date = date 
        self.number_of_guests = number_of_guests 
        self.email = email
        self.address = address 
        self.equipment_needed = equipment_needed
       

    def is_authenticated(self):
        return True

    def is_active(self):
        return True 

    def is_anonymous(self):
        return False 

    def get_id(self):
        try:
            return unicodedata(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.title) 