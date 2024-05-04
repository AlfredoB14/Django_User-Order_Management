from django.urls import path, include
from . import views

urlpatterns = [

    path('orders/', views.showOrders, name='showB'),
    path('addOrder/', views.addOrder, name='addO'),
    path('deleteOrder/<int:orderid>', views.deleteOrder, name='deleteO'),
]