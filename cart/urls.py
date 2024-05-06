from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', Cart.as_view()),
    path('cart-item/', cache_page(60)(CartItemList.as_view()), name='cart-list'),
    path('cart-item/<int:cart_id>/', cache_page(60)(CartItemListId.as_view()), name='cart-id'),
    path('cart-item/edit/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view()),


]
