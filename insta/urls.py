from django.urls import path, include
from .views import PostListView
app_name = 'insta'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('saved/', saved_posts, name='saved_posts'),
]