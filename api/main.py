from flask import Flask
from flask_restful import Api
from routes import configure_routes

app = Flask(__name__)
api = Api(app)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
