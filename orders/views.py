from django.contrib.admin import action
from django.shortcuts import render
from django.contrib.auth.models import PermissionsMixin


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.models import Rating, Likes
from orders.serializers import CreateRatingSerializer, LikeSerializer


class AddStarRatingView(PermissionsMixin, ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)



class LikesView(PermissionsMixin, ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

    @action(detail=False, methods=['get'])
    def favorite(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(author=request.user)
        serializer = LikeSerializer(queryset, many=True,
                                    context={'request': request})
        return Response(serializer.data, status=200)
