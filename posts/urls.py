from django.urls import path
from .views import *

app_name = 'posts'


urlpatterns = [
    path('create/<int:category_id>/', PostCreateView.as_view()), # 게시글 작성
    path('image/upload/<int:post_id>/', PostImageUploadView.as_view()), # 이미지 업로드
    path('update/<int:post_id>/', PostUpdateView.as_view()), # 게시글 수정
    path('delete/<int:post_id>/', PostDeleteView.as_view()), # 게시글 삭제
    path('detail/<int:post_id>/', PostDetailView.as_view()), # 게시글 세부사항
    path('list/<int:category_id>/', PostListView.as_view()), # 카테고리별 게시글 목록
    path('like/<int:post_id>/', PostLikeView.as_view()), # 좋아요 등록/취소
    path('search/words/', PostWordSearchView.as_view()), # 문장으로 게시글 검색
    path('search/hashtag/<hashtag_id>/', PostTagSearchView.as_view()), # 해시태그로 게시글 검색
]