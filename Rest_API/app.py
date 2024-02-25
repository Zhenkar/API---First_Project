from flask import Flask 
from flask_smorest import Api
import os
#Hello Git Hub

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint

import models
from variables import variables


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPOGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] ="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")         # the sqlite:///data.db will create a file called data.db , and our data will be stored there
    app.config["SQLALCHEMY_TRACK_NOTIFICATION"] = False                                                     # increases the spped of sqlalchemy
    variables.init_app(app)                                                                                 # it initializes (assigns the value) the flask_sqlalchemy extension giving it our Flask app so that it can connect the flask app to sqlalchemy , we still have to make changes to the items and store.py in the resources folder


    api = Api(app)


    with app.app_context():
        variables.create_all()  #if the tables does not exitst , this'll run or else it'll not run
                                #sqlalchemy know what models to create because we have imported ItemModel and Storemodel

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app