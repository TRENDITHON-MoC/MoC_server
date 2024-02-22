from django.urls import path
from .views import *

app_name = 'posts'


urlpatterns = [
    path('create/<str:category_name>/', PostCreateView.as_view()), # 게시글 작성
    path('image/upload/<int:post_id>/', PostImageUploadView.as_view()), # 이미지 업로드
    path('update/<int:post_id>/', PostUpdateView.as_view()), # 게시글 수정
    path('delete/<int:post_id>/', PostDeleteView.as_view()), # 게시글 삭제
    path('detail/<int:post_id>/', PostDetailView.as_view()), # 게시글 세부사항
]