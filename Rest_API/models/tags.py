from variables import variables

class TagsModel(variables.Model):
    __name__ = "tag"

    tag_id = variables.Column(variables.Integer , primary_key = True)
    tag_name = variables.Column(variables.String , unique = True , nullable = False)
    store_id = variables.Column(variables.Integer , variables.ForeginKey("store.id") , nullable = False , unique = False)
    store = variables.relationship("StoreModel" , back_populates = "tags")          #here you are trying to get the entire store elements, thats why its realtionsip ig, and foreginkey
    