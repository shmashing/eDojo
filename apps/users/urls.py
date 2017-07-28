from django.conf.urls import url
from . import views

app_name='users'
urlpatterns = [
  url(r'^$', views.index, name='home'),
  url(r'edit_account$', views.edit_user, name='editUser'),
  url(r'^log_in$', views.log_in, name='login'),
  url(r'^logout$', views.logout, name='logout'),
  url(r'^register$', views.register, name='register'),
  url(r'^register/add_user$', views.add_user, name='addUser'),
]
