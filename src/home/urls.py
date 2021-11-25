from django.urls import path
from . import views 
app_name = 'core' 
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name="signup"),
    path('postlogin/', views.postlogin, name='postlogin'),
    path('postsignup/', views.postsignup, name='postsignup'),
    path('add/', views.create, name='create'),
    path('added/', views.added, name='created'),
]