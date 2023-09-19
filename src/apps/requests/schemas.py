from src.extensions.ma import ma
from .models import Requests

class RequestOut(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Requests
