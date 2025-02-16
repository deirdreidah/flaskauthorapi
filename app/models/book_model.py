class Book:
    def __init__(self, id,title,price,description,isbn,image,no_of_pages,price_unit,publication_date,format, genre, language):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String)
     price = db.Column(db.String)
     description= db.Column(db.String)
     isbn = db.Column(db.String)
     image = dd.Column(db.img)
     no_of_pages = db.Column(db.String)
     price_unit= db.Column(db.String)
     publication_date = db.Column(db.String)
     format= db.Column(db.String)
     genre= db.Column(db.String)
     language= db.Column(db.String)