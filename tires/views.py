from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from tires.serializers import *
from .models import *
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import generics, mixins
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Favorite
from .serializers import FavoriteSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import action

class Categoryviewid(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.filter(id=self.kwargs["cat_id"])


class Categoryview(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer


class Tiresview(generics.ListCreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresSerializer


class Tiresviewid(generics.ListCreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresidSerializer

    @swagger_auto_schema(
        tags=['Tires'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность посмотреть детально "
                              "текущий товар по id. ",
    )
    def get_queryset(self, *args, **kwargs):
        return Tires.objects.filter(id=self.kwargs["tir_id"])


class ReviewsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = Reviewsserializer

    def post(self, request, *args, **kwargs):
        serializer = Reviewsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Reviews.objects.filter(id=self.kwargs["pk"])
        else:
            return Reviews.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TiresCreateAPIView(generics.CreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresCreateSerializer
    # permission_classes = [IsAdminUser]

class DeleteTiresView(generics.DestroyAPIView):
    queryset = Tires.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'tir_id'

    def perform_destroy(self, instance):

        if self.request.user == instance.user:
            instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:

            raise PermissionDenied("You do not have permission to delete this tires.")



class FavoriteView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add(self, request, tir_id=None):
        tires = Tires.objects.get(tir_id=tir_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, tires=tires)
        if created:
            return Response({'status': 'Tires added to favorites'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'Tires was already in favorites'}, status=status.HTTP_409_CONFLICT)

class RemoveFavoriteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    #permission_classes = [IsAuthenticated]

    def delete(self, request, tir_id=None):

        try:
            tires = Tires.objects.get(tir_id=tir_id)
            favorite = Favorite.objects.filter(user=request.user, tires=tires)

            if favorite.exists():
                favorite.delete()
                return Response({'status': 'Tires removed from favorites'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'status': 'Tires not found in favorites'}, status=status.HTTP_404_NOT_FOUND)

        except Tires.DoesNotExist:
            return Response({'status': 'Tires not found'}, status=status.HTTP_404_NOT_FOUND)

