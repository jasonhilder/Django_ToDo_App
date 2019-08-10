from django.urls import path
from . import views 



#urls for the main(site shell) app 

urlpatterns = [

path('', views.home, name='home'),
path('mylists/', views.myLists, name='mylists'),
path('<int:id>', views.listItems, name='listItems'),
path('welcome/', views.new_user_welcome, name='Welcome new user'),

] 