from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="log"),
    path('logout_user/', views.logout_user, name="logt"),
    path('register_user/', views.register_user, name="register")
]