from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logoutpage, name='logoutpage'),
]
