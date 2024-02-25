from variables import variables


class TagItem(variables.Model):
    __name__ = "items_tags"

    id = variables.Column(variables.Interger, primary_key = True)
    item_id = variables.Column(variables.Integer , variables.ForegienKey("item.id"))
    tag_id = variables.Column(variables.Integer , variables.ForegienKey("tag.id"))