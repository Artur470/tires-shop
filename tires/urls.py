from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *


urlpatterns = [

    path('category/<int:cat_id>/', Categoryviewid.as_view()),
    path('category/', Categoryview.as_view()),
    path('list/<int:tir_id>/', cache_page(60)(Tiresviewid.as_view())),
    path('list/', cache_page(60)(Tiresview.as_view())),
    path('create/', TiresCreateAPIView.as_view()),
    path('reviews/add/', cache_page(60)(Reviewsadd.as_view())),
    path('list/remove/<int:tir_id>/', DeleteTiresView.as_view()),
    path('reviews/remove/<int:pk>/', ReviewDeleteAPIView.as_view()),
    path('reviews/<int:pk>/', cache_page(60)(Reviewsview.as_view())),
    path('favorites/add/', AddToFavoritesView.as_view(), name='add_to_favorite'),
    path('favorites/remove/<int:tir_id>/', RemoveFromFavoriteView.as_view(), name='remove_from_favorite'),
    path('favorites/', ListFavoriteView.as_view(), name='list_favorites'),
]

