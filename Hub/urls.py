from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('signup/',views.signup, name = 'signup'),
    path('login/', views.logins, name = 'login'),
    path('', views.home, name = 'home'),
    path('logout/', views.logout_view, name='logout'),
    path('MovieDetail/<id>', views.movie_detail, name='moviedetail'),
    path('UserList/', views.user_list,name='userlist'),
    path('MovieList/', views.MovieView,name='movielist'),
    path('UserUpdate/<str:pk>/', views.user_update, name='userupdate'),
    path('MovieUpdate/<str:pk>/', views.movie_update, name='movieupdate')

]