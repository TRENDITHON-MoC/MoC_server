from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.posts_serializers import *
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from django.db.models import Q


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
    

class PostWordSearchView(APIView):
    """
    문장으로 게시글 검색
    """
    def post(self, request):
        word_list = request.data.get('word_list')

        query = Q()

        for keyword in word_list:
            query |= Q(body__icontains=keyword) | Q(title__icontains=keyword)

        posts = Post.objects.filter(query).order_by('-created_at')
        paginator = PostPageNumberPagination()
        page = paginator.paginate_queryset(posts, request)

        serializer = PostListSerializer(page, context = {'request':request}, many = True)
        return paginator.get_paginated_response(serializer.data)
    

class PostTagSearchView(APIView):
    """
    같은 해시태그를 갖는 게시글 검색
    """
    def get(self, request, hashtag_id):
        hashtag = Hashtag.objects.prefetch_related('posts').get(pk = hashtag_id)
        posts = hashtag.posts.all()
        serializer = PostListSerializer(posts, many = True)
        
        paginator = PostPageNumberPagination()
        page = paginator.paginate_queryset(posts, request)

        serializer = PostListSerializer(page, context = {'request':request}, many = True)
        return paginator.get_paginated_response(serializer.data)