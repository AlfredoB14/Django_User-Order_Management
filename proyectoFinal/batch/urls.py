from django.urls import path, include
from . import views

urlpatterns = [

    path('orders/', views.showOrders, name='showB'),
    path('addOrder/', views.addOrder, name='addO'),
    path('deleteOrder/<int:orderid>', views.deleteOrder, name='deleteO'),
    path('modifyOrder/<int:orderid>', views.modifyOrder, name='modifyO'),
    path('viewOrder/<int:orderid>', views.viewOrder, name='viewO'),
    path('nextStage/<int:orderid>', views.nextStage, name='nextS'),


]