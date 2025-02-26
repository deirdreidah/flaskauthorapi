from flask import Flask 
from app.extensions import db

#Application Factory Function
def create_app():
    app = Flask(__name__)
    db.init_app(app)

    #index route
    @app.route('/')
    def home():
      return "Hello."
    

    return app