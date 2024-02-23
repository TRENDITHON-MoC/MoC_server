from django.urls import path
from .views import *

app_name = 'daily'


urlpatterns = [
    path('select/', PopularTestView.as_view()),
    path('popular/yesterday/', PopularPostView.as_view()),
]