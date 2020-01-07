from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 

# Create your views here.

def register(request):
    if request.method == 'POST':
        print("This is working bro.")
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username,"This is working")
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('/')
    else:
        #If there is no a post request just send an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


