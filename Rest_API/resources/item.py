import uuid 
#from flask import request
from flask_smorest import Blueprint , abort
from flask.views import MethodView
#from variables import items , store

from schema import Itemsvalidate , ItemsUpdate



blp = Blueprint("Items" , __name__ , description = "Operations on Item")


@blp.route("/items/<string:item_id>")
class Item(MethodView):

    @blp.response(200 , Itemsvalidate)                                                      # this line @blp.response uses scheme that we defined and show the values that are defined in the scheme , you define with status code what message you want
    def get(self, item_id):                                                                 # get_specific_item                                                              
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="item not found")

    def delete(self, item_id):                                                              # delete_item
        try:
            del items[item_id]
            return {"message" : "item deleted"}
        except KeyError:
            abort(404 , message = " item not found")


    #order of argument and response matters
    @blp.arguments(ItemsUpdate)                 
    @blp.response(200 , Itemsvalidate)
    def put(self, request_data , item_id):                                                  # update_item , the request_data shoule be first because its the rule for arguments keyword                              
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


    #the above schemas were for single item, but for multiple items 
    @blp.response(200 , Itemsvalidate(many = True))
    def get(self):
        #before return {"items" : list(items.values())}
        #after schema -  no need for converting the dict to list as the marsmello does it for us
        return items.values()   
    

    @blp.arguments(Itemsvalidate)                                                                       # this line is making sure that the json text contains all the necessary fields mentioned in the schema , and returns a dcitonary (in our case request_data) no need for request_dat = reqest.get_json()
    @blp.response(201,Itemsvalidate)
    def post(self, request_data):                                                                       # create a new item
 

        # This for loop is needed cause the marsmello dosen't check whether the data alreday exists
        for i in items.values():                                                                        # there will be many dict inside items - 1:{} , 2,{} , 3{} so if you do values loop , you will get {} of 1 , {} of2 . 
            if (request_data["name"] == i["name"] and request_data["price"] == i["price"]):             # thats why i["name"] is possible in the first loop you will get value of 1 key - meaning - {} 
                abort(400 ,message = "Item already exists")

        if request_data["store_id"] not in store:                                                       # in will only the key value in the dictionary
            abort(404 , message = "store not found")

        item_id = uuid.uuid4().hex
        new_data = {**request_data , "item_id" : item_id}
        items[item_id] = new_data

        return {"item" : new_data} ,201