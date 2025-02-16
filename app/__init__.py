from flask import Flask 

#Application Factory Function
def create_app():
    app = Flask(__name__)

    #index route
    @app.route('/')
    def home():
      return "Hello."

    return app