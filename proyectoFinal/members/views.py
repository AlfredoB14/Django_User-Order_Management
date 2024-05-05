from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_user(request):

    if request.user.is_authenticated:

        return redirect('home')
    
    else:

        if request.method == "POST":

            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                messages.success(request, ("Successfully logged in"))
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, ("Credentials not valid"))
                return redirect('log')


        else:
            return render(request, 'authenticate/login.html', {})
    
@login_required(login_url="/members/login_user/")
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('home')


def register_user(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))

            return redirect('home')
        
        else:
            form = UserCreationForm()
            messages.success(request, ("Error with register"))
            return render(request, 'authenticate/register_user.html', {
                'form':form,
            })

    else:
        form = UserCreationForm()
        return render(request, 'authenticate/register_user.html', {
            'form':form,
        })
    
def userManagement(request):

    if request.user.is_authenticated:

        users = User.objects.all()
        return render(request, 'authenticate/userManagement.html', {'users': users})

    else:
        messages.success(request, ("You don't have permission to do that!"))
        return redirect('home')
    

def delete_user(request, userid):

    if request.user.is_authenticated:

        user = User.objects.get(pk=userid)

        if request.user.id == userid or request.user.is_staff:

            messages.success(request, ("The user was Deleted Successfully"))
            user.delete()
            logout(request)
            return redirect('home')
        
        else:
            messages.success(request, ("You don't have permission to do that!"))
            return redirect('home')   

    else:
        messages.success(request, ("You are not logged in"))
        return redirect('home')

def modify_user(request, userid):
    pass