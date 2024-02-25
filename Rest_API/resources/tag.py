from variables import variables
from flask_smorest import abort , Blueprint
from flask.views import MethodView

from models import ItemModel , StoreModel , TagsModel
from sqlalchemy.exc import SQLAlchemyError , IntegrityError
from schema import Tagvalidate


blp = Blueprint("Tags", "tags", description = "Operation on Tags")

@blp.route("/store/<string:store_id>/tag")
class Tags(MethodView):
    
    @blp.response(200,Tagvalidate(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    @blp.response(200,Tagvalidate)
    @blp.arguments(Tagvalidate)
    def post(self,tag_data , store_id):
        # You can also do this
        # TagsModel.query.filter(TagsModel.store_id == "store_id" , TagsModel.name == tag_data["name"].first())
        tag = TagsModel(**tag_data , store_id = store_id)
        try:
            variables.session.add(tag)
            variables.session.commit()
        except SQLAlchemyError:
            abort(400 , message="Something went wrong while creating the tag")
        
        return tag

@blp.route("/tag/<string:tag_id>")
class Tags2(MethodView):
    @blp.response(200, Tagvalidate)
    def get(tag_id):
        tag = TagsModel.query.get_or_404(tag_id)
        return tag