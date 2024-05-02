from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.


user = get_user_model()
def home(request):

    if request.user.is_authenticated and request.user.is_staff:

        return render(request, 'events/adminHome.html', {})
    
    else:
        return render(request, 'events/home.html', {})