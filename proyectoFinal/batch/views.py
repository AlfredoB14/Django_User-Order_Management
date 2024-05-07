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

                if form.flavour == 'strawberry':
                    form.total = (form.boxes * form.units_per_box) * 15
                elif form.flavour == 'blueberry':
                    form.total = (form.boxes * form.units_per_box) * 20

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
    


def modifyOrder(request, orderid):

    if request.user.is_authenticated:

        order =  Batch.objects.get(pk=orderid)

        if order.orderOwner == request.user or request.user.is_staff:
            
            form = batchForm(request.POST or None, instance=order)

            if form.is_valid():

                form = form.save(commit=False)
                if form.flavour == 'strawberry':
                    form.total = (form.boxes * form.units_per_box) * 15
                elif form.flavour == 'blueberry':
                    form.total = (form.boxes * form.units_per_box) * 20

                form.save()
                return redirect('showB')

            return render(request, 'batch/modifyOrder.html', {'order':order, 'form':form})
        
        else:
            messages.success(request, ("You don't have permission to do that!"))
            return redirect('home')   
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')
    

def viewOrder(request, orderid):

    if request.user.is_authenticated:

        order =  Batch.objects.get(pk=orderid)

        if order.orderOwner == request.user or request.user.is_staff:
            
            return render(request, 'batch/viewOrder.html', {'batch':order})

        else:   
            messages.success(request, ("You don't have permission to do that!"))
            return redirect('home') 
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')
    

def nextStage(request, orderid):

    if request.user.is_authenticated and request.user.is_staff:

        order = Batch.objects.get(pk=orderid)

        if order.status == 'Confirmation':
            order.status = 'Packaging'
            order.save()

            return redirect('viewO', orderid)
        
        elif order.status == 'Packaging':
            order.status = 'Shipping'
            order.save()
            
            return redirect('viewO', orderid)

        elif order.status == 'Shipping':
            order.status = 'Completed'
            order.save()

            return redirect('viewO', orderid)
        
        else:
            messages.success(request, ("The order has already been completed"))
            return redirect('viewO', orderid)

    else:   
        messages.success(request, ("You don't have permission to do that!"))
        return redirect('home') 
