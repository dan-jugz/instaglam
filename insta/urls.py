from django.urls import path, include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,saved_posts,PostLikeToggle
app_name = 'insta'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(),name='post_create'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update'), 
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:id>/likes/', PostLikeToggle.as_view(), name='like_toggle'),
    path('saved/', saved_posts, name='saved_posts'),
]