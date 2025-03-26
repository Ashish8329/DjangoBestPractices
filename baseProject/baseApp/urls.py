from django.urls import path, include
from .views import hell_world, HelloWorldView, HelloWorldAPI, hello_world_apiview

urlpatterns = [
    path('/fbv',hell_world, name="FBV_view"),
    path('/cbv',HelloWorldView.as_view(), name="CBV_views"),
    path('/api_view', HelloWorldAPI.as_view(), name="DRF_APIView"),
    path('/fbv_apiview',hello_world_apiview, name="FBV_viewapiview"),
]