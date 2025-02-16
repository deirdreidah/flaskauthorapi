class Author:
    def __init__(self, id, first_name, last_name, contact, email, password , image,bio,createdat):
      id = db.Column(db.Integer, primary_key=True)
      first_name = db.Column(db.String(20))
      last_name = db.Column(db.String(20))
      contact = db.Column(db.String(10))
      email = dd.Column(db.String(30))
      password = db.Column(db.String(8))
      image = db.Column(db.Img)
      bio = db.Column(db.String)
      createdat = db.Column(db.String)
