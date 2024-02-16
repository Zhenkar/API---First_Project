from variables import variables

class StoreModel(variables.Model):
    __tablename__= "store"

    id = variables.Column(variables.Integer, primary_key = True)
    name = variables.Column(variables.String , nullable = False)