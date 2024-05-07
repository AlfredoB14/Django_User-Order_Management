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
        return render(request, 'events/adminHome.html', {'users':users, 'orders':orders})
    
    else:
        return render(request, 'events/home.html', {})
    

