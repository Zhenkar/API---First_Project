from variables import variables

class ItemModel(variables.Model):
    __tablename__= "items"


    id = variables.Column(variables.Integer , primary_key = True)
    name = variables.Column(variables.String(50) , uniqe = True ,nullable = False)
    price = variables.Column(variables.Float , unique = False , nullable = False)
    store_id = variables.Column(variables.Integer ,variables.ForeignKey("store.id")  , unique= True , nullables = False)  # Foregin key - tablename . column name (id)