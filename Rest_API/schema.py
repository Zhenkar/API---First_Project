from marshmallow import Schema , fields

class PlainItemsvalidate(Schema):
    id = fields.Int(dump_only = True)                   # dump_only because , you are not receving id data from the user to be validated, you are generating the id and just want to send when there is a get requrest , so you only dump it when asked.
    name = fields.Str(required=True)                 # It is a field that you take from user through json, so you give a required field for it
    price = fields.Float(required = True)
    # store_id = fields.String(required= True)


class PlainStorevalidate(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required = True)

class ItemsUpdate(Schema):
    name = fields.Str()
    price = fields.Float()

class Itemsvalidate(PlainItemsvalidate):
    store_id = fields.Int(requreied="True" , load_only=True)
    store = fields.Nested(PlainStorevalidate() , dump_only=True)                        # Schemas can be nested to represent relationships between objects (e.g. foreign key relationships)

class Storevalidate(PlainStorevalidate):
    items = fields.List(fields.Nested(PlainItemsvalidate()),dump_only=True)             #When you are going to display the store , it should also display the itmes it's associated with it
                                                                                        # so you are giving it as list - for the n number of items to be displayed as list