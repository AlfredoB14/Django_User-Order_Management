from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from batch.models import Batch
# Create your views here.


user = get_user_model()
def home(request):

    
    if request.user.is_authenticated and request.user.is_staff:

        users = User.objects.all()
        orders = Batch.objects.all()


        totals = 0
        total_confirm = 0
        total_packaging=0
        total_shipping=0
        total_completed=0
        for order in orders:
            totals += order.total

            if order.status == "Confirmation":
                total_confirm+=1

            elif order.status == "Packaging":
                total_packaging+=1

            elif order.status == "Shipping":
                total_shipping+=1
            
            elif order.status == 'Completed':
                total_completed+=1

        return render(request, 'events/adminHome.html', {'users':users, 'orders':orders, 'totals':totals, 'confirm':total_confirm, 'packaging':total_packaging, 'shipping':total_packaging, 'completed':total_completed})
    
    else:
        return render(request, 'events/home.html', {})
    
