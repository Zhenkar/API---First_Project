from variables import variables

class StoreModel(variables.Model):
    __tablename__= "store"

    id = variables.Column(variables.Integer, primary_key = True)
    name = variables.Column(variables.String , nullable = False)

    items = variables.relationship("ItemModel" , back_populates="store" , lazy="dynamic")

    # now we have a item attribute[column] in the StoreModel class , the string "stores"  [ item  = variable.relationship(back_populate = stores)] 
    # refers that to the attribute stores in the class ItemModel