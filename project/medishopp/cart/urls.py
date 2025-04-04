from django.urls import path
from .views import CartListView, AddToCartView, UpdateCartItemView, DeleteCartItemView, ClearCartView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('update/<int:pk>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('remove/<int:pk>/', DeleteCartItemView.as_view(), name='remove-cart-item'),
    path('clear/', ClearCartView.as_view(), name='clear-cart'),
]
