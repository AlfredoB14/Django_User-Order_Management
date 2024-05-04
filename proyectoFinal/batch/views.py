from django.shortcuts import render, redirect
from .models import Batch
from django.contrib.auth.models import User
from .forms import batchForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def showOrders(request):

    
    if request.user.is_authenticated:
        batches = Batch.objects.all()
        users = User.objects.all()

        return render(request, 'batch/orders.html', {'batches':batches, "users":users})
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')
    
def addOrder(request):

    if request.user.is_authenticated:

        if request.method == "POST":
            form = batchForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.orderOwner = request.user
                form.save()

                messages.success(request, ("Order Placed Successfully"))
                return redirect('showB')
            
        form = batchForm
        return render(request, 'batch/addOrder.html', {'form':form})
    
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')
    
def deleteOrder(request, orderid):

    if request.user.is_authenticated:

        order = Batch.objects.get(pk=orderid)

        if request.user == order.orderOwner or request.user.is_staff:

            messages.success(request, ("The order was Deleted Successfully"))
            order.delete()

            return redirect('showB')
        
        else:
            messages.success(request, ("You don't have permission to do that!"))
            return redirect('home')   

    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')