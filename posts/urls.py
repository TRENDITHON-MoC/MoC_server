from django.urls import path
from .views import *


urlpatterns = [
    path('create/<str:category_name>/', PostCreateView.as_view()),
]