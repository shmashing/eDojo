from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='home'),
  url(r'^explore$', views.explore, name='explore'),
  url(r'^myShops$', views.my_shops, name='myStores'),
]
