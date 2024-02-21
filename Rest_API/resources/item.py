import uuid 
from flask_smorest import Blueprint , abort
from flask.views import MethodView

#for marshmallow validation of the data incoming and outgoing
from schema import Itemsvalidate , ItemsUpdate

#for sql alchemy - database object and sqlalchemy error
from variables import variables
from sqlalchemy.exc import SQLAlchemyError
from models import ItemModel



blp = Blueprint("Items" , __name__ , description = "Operations on Item")


@blp.route("/items/<string:item_id>")
class Item(MethodView):

    @blp.response(200 , Itemsvalidate)                                                      # this line @blp.response uses scheme that we defined and show the values that are defined in the scheme , you define with status code what message you want
    def get(self, item_id):                                                                                                                              
        item = ItemModel.query.get_or_404(item_id)
        return item


    def delete(self, item_id):                                                              
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Delete still not implemented")


    #order of argument and response matters
    @blp.arguments(ItemsUpdate)                 
    @blp.response(200 , Itemsvalidate)
    def put(self, request_data , item_id):                                                  # update_item , the request_data shoule be first because its the rule for arguments keyword                              
        item = ItemModel.query.get(item_id) 
        if item:
            item.name = request_data["name"]
            item.price = request_data["price"]
        else:
            item = ItemModel(id = item_id ,**request_data)
        variables.session.add(item)
        variables.session.commit()
        return item
        
        




@blp.route("/items")
class Items_new(MethodView):


    #the above schemas were for single item, but for multiple items 
    @blp.response(200 , Itemsvalidate(many = True))
    def get(self):
        return items.values()   
    

    @blp.arguments(Itemsvalidate)                                                           # this line is making sure that the json text contains all the necessary fields mentioned in the schema , and returns a dcitonary (in our case request_data) no need for request_dat = reqest.get_json()
    @blp.response(201,Itemsvalidate)
    def post(self, request_data):                                              
        item = ItemModel(**request_data)                                                    #I am referencing item table through the ItemModel class, **request_data says that the dictionary value which I will receive will be seperated as variable & value respectively with the table columns defined in the item table 

        try:
            variables.session.add(item)
            variables.session.commit()
        except SQLAlchemyError:
            abort ( 500 , message = " Someting went wrong while inserting the data ")

        return item