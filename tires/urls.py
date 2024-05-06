from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *


urlpatterns = [

    path('category/<int:cat_id>/', Categoryviewid.as_view()),
    path('category/', Categoryview.as_view()),
    path('list/<int:tir_id>/', cache_page(60)(Tiresviewid.as_view())),
    path('list/', cache_page(60)(Tiresview.as_view())),
    path('create/', TiresCreateAPIView.as_view()),
    path('reviews/<int:pk>/', cache_page(60)(ReviewsView.as_view())),
    path('favorite/', cache_page(60)(FavoriteView.as_view()), name='favorite-list'),
    path('favorite/remove/<int:tir_id>/', RemoveFavoriteView.as_view(), name='remove-from-favorites'),
    path('list/remove/<int:tir_id>/', DeleteTiresView.as_view())
]

