from django.shortcuts import render

from django_filters import rest_framework as filters
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from products.models import Product, Comment, Likes
from products.permissions import IsAuthorOrIsAdmin, IsAuthor
from products.serializers import CreateProductSerializer, ProductListSerializer, ProductDetailSerializer, \
    CommentSerializer, LikeSerializer
from rest_framework import filters as rest_filters


class ProductFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()
    class Meta:
        model = Product
        fields = ('status', 'created_at')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthorOrIsAdmin, ]
    filter_backends = [filters.DjangoFilterBackend,
                       rest_filters.SearchFilter,
                       rest_filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'text']
    ordering_fields = ['created_at', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer


class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_context(self):
        return {'request': self.request}


class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]


class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]


class LikesView(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

    @action(detail=False, methods=['get'])
    def favorite(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(author=request.user)
        serializer = LikeSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(serializer.data, status=200)
