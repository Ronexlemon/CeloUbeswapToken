from django.urls import path,include
from . import  views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('ubeswap',views.UbeListView,basename="ubeswaptokens")
urlpatterns = [
    path("",include(route.urls))]