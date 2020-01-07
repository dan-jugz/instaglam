from django.urls import path, include
from .views import PostListView,PostDetailView,PostCreateView
app_name = 'insta'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(),name='post_create'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'), 
    path('saved/', saved_posts, name='saved_posts'),
]