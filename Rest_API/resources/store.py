import uuid 
from flask import request
from flask_smorest import Blueprint , abort
from flask.views import MethodView
from variables import store

from schema import Storevalidate


blp = Blueprint("store",__name__, description = "Operations on store")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):                                                             #get particular store
        try:
            return store[store_id]
        except KeyError:
            abort(404 , message = "store not found")
    

    def delete(self , store_id):                                                        #delete a particular store
        try:
            del store[store_id]
            return {"message" : "store deleted"}
        except KeyError:
            abort(404 , message = " store not found")
        
@blp.route("/store")
class Store_new(MethodView):

    def get(self):                                                                      #get all stores
        return {"stores" : list(store.values())}

    @blp.arguments(Storevalidate)
    def post(self, store_data):                                                         #insert_new_store , the Storevalidate will return a dict so no need for store_data = request.get_json()
    
        if ("name" not in store_data):
            abort(400 , message = "You must add name variable inside the request")

        for i in store.values():
            if ( store_data["name"] == i["name"]):
                abort(400, message = "The store already exist")

        store_id = uuid.uuid4().hex 
        new_data = {**store_data , "store_id":store_id}
        store[store_id ] = new_data
        return new_data , 201