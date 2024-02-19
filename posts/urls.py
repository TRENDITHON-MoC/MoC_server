from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]