import uuid 
from flask import request
from flask_smorest import Blueprint , abort
from flask.views import MethodView

#for validation using marshmallow
from schema import Storevalidate

#importing the table, sql object , error handler for sqlalchemy
from models import StoreModel
from variables import variables
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("store",__name__, description = "Operations on store")


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200 , Storevalidate)
    def get(self,store_id):                                                             #get particular store
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self , store_id):                                                        #delete a particular store
        store = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("delete not implemented yet")
        
@blp.route("/store")
class Store_new(MethodView):

    @blp.response(200,Storevalidate(many = True))
    def get(self):                                                                      #get all stores
        #before -> return {"stores" : list(store.values())}
        store.values()

    
    @blp.response(201 , Storevalidate)
    @blp.arguments(Storevalidate)
    def post(self, store_data):                                                         #insert_new_store , the Storevalidate will return a dict so no need for store_data = request.get_json()
        store = StoreModel(**store_data)
        try:
            variables.session.add(store)
            variables.session.commit()
        except IntegrityError:
            abort (400, message="A store with the same name already exists")
        except SQLAlchemyError:
            abort (500 , message="Something went wrong while createing the store")
        
        return store 