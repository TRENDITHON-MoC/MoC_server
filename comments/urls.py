from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:post_id>/', CommentCreateView.as_view(), name='comment-list-create'),
    path('delete/<int:comment_id>/', CommentDeleteView.as_view(), name='comment-list-delete'),
]