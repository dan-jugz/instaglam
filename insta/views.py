from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse 
from datetime import datetime
from django.utils import timezone
from .models import Post 
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):

    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = 'posts'