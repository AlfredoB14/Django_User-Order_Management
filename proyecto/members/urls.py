from django.urls import path, include
from . import views

urlpatterns = [
    
    path('login_user/', views.login_user, name="log"),
    path('logout_user/', views.logout_user, name="logt"),
    path('register_user/', views.register_user, name="register"),
    path('manage_user/', views.userManagement, name="manage"),
    path('delete_user/<int:userid>', views.delete_user, name='deleteU'),
    path('modify_user/<int:userid>', views.modify_user, name='modifyU'),

]