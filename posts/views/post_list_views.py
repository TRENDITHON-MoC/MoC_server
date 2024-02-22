from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.posts_serializers import *
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


class PostPageNumberPagination(PageNumberPagination):
    """
    페이지네이션 클래스
    """
    page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('pageCnt', self.page.paginator.num_pages),
            ('curPage', self.page.number),
            ('postList', data),
        ]))


class PostListView(APIView):
    """
    게시글 리스트 뷰
    """
    def get(self, request, category_id):
        posts = Post.objects.filter(category__pk = category_id).order_by('-created_at')
        paginator = PostPageNumberPagination()
        page = paginator.paginate_queryset(posts, request)

        serializer = PostListSerializer(page, context = {'request':request}, many = True)
        return paginator.get_paginated_response(serializer.data)