from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers.posts_serializers import *
from django.shortcuts import get_object_or_404

