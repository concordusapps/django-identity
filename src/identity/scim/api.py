
from tastypie.api import Api
from . import views

v1_api = Api(api_name='v1')

v1_api.register(views.User())
