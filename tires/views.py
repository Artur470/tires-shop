from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from tires.serializers import *
from .models import *
import requests
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework import generics, mixins
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import action
from django.db.models import Count
from django.http import HttpResponseServerError



class Categoryviewid(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.filter(id=self.kwargs["cat_id"])


class Categoryview(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer


class Tiresview(generics.ListAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresSerializer


class Tiresviewid(generics.ListAPIView):
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



class Reviewsview(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Reviews.objects.filter(id=self.kwargs["pk"])
        else:
            return Reviews.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')



    def post(self, request, *args, **kwargs):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reviewsadd(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = Reviewsaddserializer

class ReviewDeleteAPIView(generics.DestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Reviews.objects.filter(id=self.kwargs["pk"])
        else:
            return Reviews.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')

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

class AddToFavoritesView(generics.CreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Tires added to favorites'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user_favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(user_favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class RemoveFromFavoriteView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        user = request.user
        tir_id = kwargs.get('tir_id')

        try:
            favorite = Favorite.objects.get(user=user, tir_id=tir_id)
            favorite.delete()
            return Response({"message": "Tires removed from favorites"}, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            return Response({"message": "Tires not found in favorites"}, status=status.HTTP_404_NOT_FOUND)


class ListFavoriteView(generics.ListAPIView):
    serializer_class = TiresSerializer

    def get_queryset(self):
        user = self.request.user
        # Получаем избранные товары для текущего пользователя
        favorites = Favorite.objects.filter(user=user)
        tir_ids = favorites.values_list('tir_id', flat=True)  # Получаем список id товаров из избранного
        return Tires.objects.filter(id__in=tir_ids)
