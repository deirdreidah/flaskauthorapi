from app.extensions import db
from datetime import datetime

class Book(db.Model):
     book_id = db.Column(db.Integer, primary_key=True, nullable = False)
     title = db.Column(db.String(30), nullable = False)
     price = db.Column(db.String(20), nullable = False)
     description= db.Column(db.String(250), nullable = False)
     isbn = db.Column(db.String(200), nullable = False)
     image = db.Column(db.String(255), nullable = False, unique = True)
     no_of_pages = db.Column(db.String(5), nullable = False)
     price_unit= db.Column(db.String(20), nullable = False)
     publication_date = db.Column(db.String(35), nullable = False)
     format= db.Column(db.String(50), nullable = False)
     genre= db.Column(db.String(50), nullable = False)
     language= db.Column(db.String(50), nullable = False)

     def __init__(self, book_id,title,price,description,isbn,image,no_of_pages,price_unit,publication_date,format, genre, language):
       self.book_id = book_id
       self.title = title
       self.price = price
       self.description= description
       self.isbn = isbn
       self.image = image
       self.no_of_pages = no_of_pages
       self.price_unit= price_unit
       self.publication_date = publication_date
       self.format= format
       self.genre= genre
       self.language= language