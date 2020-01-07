from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.views.generic import DetailView

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


class Profile(DetailView):
    template_name = 'users/profile.html'
    queryset = User.objects.all()
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        return user 
        
    def get_context_data(self, *args, **kwargs):
        context = super(Profile,self).get_context_data(*args, **kwargs)
        
        user = self.get_object()
        context.update({
            'posts' : user.posts.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
        })
        return context 

    def add_follow(self, request):
        user = self.get_object() 
        user.profile.followed_by.add(request.user.profile) 


def edit_profile(request):
    if request.method == "POST":

        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/edit_profile.html', context)
