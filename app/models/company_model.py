class Company:
    def __init__(self , id, name, origin, description , email, contact, createdat, updatedat ): 
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(20))
        origin = db.Column(db.String)
        description = db.Column(db.String)
        email =  db.Column(db.String(30))
        contact = db.Column(db.String(10))
        createdat = db.Column(db.String)
        updatedat = db.Column(db.String)
