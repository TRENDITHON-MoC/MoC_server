from django.urls import path
from .views import comment_create_view, comment_delete_view

urlpatterns = [
    path('create/<int:post_id>', comment_create_view, name='comment-list-create'),
    path('delete/<int:pk>', comment_delete_view, name='comment-list-delete'),
]