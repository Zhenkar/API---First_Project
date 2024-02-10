import uuid
from flask_smorest import abort
from flask import Flask , request
from variables import items , store

app = Flask(__name__)


@app.get("/store")
def get_all_stores():
    return {"stores" : list(store.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return store[store_id]
    except KeyError:
        abort(404 , message = "store not found")


@app.post("/store")
def create_new():
    store_data = request.get_json()
    
    if ("name" not in store_data):
        abort(400 , message = "You must add name variable inside the request")

    for i in store.values():
        if ( store_data["name"] == i["name"]):
            abort(400, message = "The store already exist")

    store_id = uuid.uuid4().hex 
    new_data = {**store_data , "store_id":store_id}
    store[store_id ] = new_data
    return new_data , 201


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del store[store_id]
        return {"message" : "store deleted"}
    except KeyError:
        abort(404 , message = " store not found")




@app.get("/items")
def get_all_items():
    return {"items" : list(items.values())}


@app.get("/items/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404 , message = "item not found")


@app.post("/items")
def create_item():
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
    

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message" : "item deleted"}
    except KeyError:
        abort(404 , message = " item not found")


@app.put("/items/<string:item_id>")                                                                # you are replacing the item with a new one
def update_item(item_id):
    request_data = request.get_json()
    if "name" not in request_data or "price" not in request_data:
        abort(400 , message = "You must inlude name and price inside the json")
    try:
        item = items[item_id]
        item |= request_data
        return item
        
    except keyError:
        abort(404 , message = "item not found")


