import uuid 
from flask import request
from flask_smorest import Blueprint , abort
from flask.views import MethodView
from variables import items , store

blp = Blueprint("Items" , __name__ , description = "Operations on Item")


@blp.route("/items/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):                                                                 # get_specific_item
        try:
            return items[item_id]
        except KeyError:
            abort(404 , message = "item not found")

    def delete(self, item_id):                                                              # delete_item
        try:
            del items[item_id]
            return {"message" : "item deleted"}
        except KeyError:
            abort(404 , message = " item not found")

    def put(self, item_id):                                                                 # update_item                               
        request_data = request.get_json()
        if "name" not in request_data or "price" not in request_data:
            abort(400 , message = "You must inlude name and price inside the json")
        try:
            item = items[item_id]
            item |= request_data
            return item
            
        except keyError:
            abort(404 , message = "item not found")



@blp.route("/items")
class Items_new(MethodView):
    def get(self):
        return {"items" : list(items.values())}
    
    def post(self):                                                                                       # create a new item
        request_data = request.get_json()
        if ("name" not in request_data or
            "price" not in request_data or
            "store_id" not in request_data):
            abort(
                400 , 
                message = "Bad request. You have to input name , price and store_id")

        for i in items.values():                                                                        # there will be many dict inside items - 1:{} , 2,{} , 3{} so if you do values loop , you will get {} of 1 , {} of2 . 
            if (request_data["name"] == i["name"] and request_data["price"] == i["price"]):             # thats why i["name"] is possible in the first loop you will get value of 1 key - meaning - {} 
                abort(400 ,message = "Item already exists")

        if request_data["store_id"] not in store:                                                       # in will only the key value in the dictionary
            abort(404 , message = "store not found")

        item_id = uuid.uuid4().hex
        new_data = {**request_data , "item_id" : item_id}
        items[item_id] = new_data

        return {"item" : new_data} ,201