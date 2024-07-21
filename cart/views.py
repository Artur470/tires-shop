from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from drf_yasg import openapi
# from drf_payments.models import BasePayment
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CartItem


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    # permission_classes = [IsAuthenticated]


class CartItemListId(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        queryset = CartItem.objects.filter(cart_id=cart_id)
        return queryset


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.cartitem_set.all()
        else:
            return CartItem.objects.none()

    def view_cart_item(request, cart_item_id):
        if request.user.is_authenticated:
            cart_item = get_object_or_404(CartItem, id=cart_item_id)

            cart_item_quantity = cart_item.quantity
            cart_item_price = cart_item.price

            return JsonResponse({'success': 'Cart item found.', 'cart_item_id': cart_item.id})
        else:
            return JsonResponse({'error': 'User is not authenticated.'}, status=403)

    @swagger_auto_schema(
        tags=['Cart'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность редактировать "
                              "текущий товар в корзине. ",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return CartItem.objects.filter(id=self.kwargs["pk"])


class Cart(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    # permission_classes = [IsAuthenticated]


class Order(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]




