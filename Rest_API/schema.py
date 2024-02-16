from marshmallow import schema , fields

class PlainItemsvalidate(schema):
    id = fields.Int(dump_only = True)                   # dump_only because , you are not receving id data from the user to be validated, you are generating the id and just want to send when there is a get requrest , so you only dump it when asked.
    name = fields.String(required=True)                 # It is a field that you take from user through json, so you give a required field for it
    price = fields.Fload(required = True)
    # store_id = fields.String(required= True)


class PlainStorevalidate(schema):
    id = fields.String(dump_only = True)
    name = fields.String(required = True)

class ItemsUpdate(schema):
    name = fields.String()
    price = fields.Float()

class ItemsValidate(PlainItemsvalidate):
    store_id = fields.Int(requreied="True" , load_only=True)
    store = fields.Nested(PlainStorevalidate() , dump_only=True)

class StoreValidate(PlainStorevalidate):
    items = fields.List(fields.Nested(PlainItemsvalidate()),dump_only=True)