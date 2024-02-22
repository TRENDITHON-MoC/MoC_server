from django.urls import path
from .views import *


urlpatterns = [
    path('create/<str:category_name>/', PostCreateView.as_view()),
    path('image/upload/<int:post_id>/', PostImageUploadView.as_view()),
]