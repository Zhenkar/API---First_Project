from variables import variables

class StoreModel(variables.Model):
    __tablename__= "stores"

    id = variables.Column(variables.Integer, primary_key = True)
    name = variables.Column(variables.String(80) , nullable = False)

    items = variables.relationship("ItemModel" , back_populates="stores" , lazy="dynamic")

    # now we have a item attribute[column] in the StoreModel class , the string "stores"  [ item  = variable.relationship(back_populate = stores)] 
    # refers that to the attribute stores in the class ItemModel