from django.urls import path
from .views import CreateOrderView, MyOrdersView, OrderDetailView, AllOrdersView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('my/', MyOrdersView.as_view(), name='my-orders'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('all/', AllOrdersView.as_view(), name='all-orders'),
]
