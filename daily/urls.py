from django.urls import path
from .views import *

app_name = 'daily'


urlpatterns = [
    path('select/', PoPularTestView.as_view()),
]