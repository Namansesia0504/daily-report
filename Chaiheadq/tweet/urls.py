from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
# from .views import BookViewSet
# router = DefaultRouter()
# router.register(r'books', BookViewSet)

urlpatterns = [
     path('',views.home,name='index.html'),
     # path('',views.tweet_list,name='tweet_list'),
     path('tweet/', views.tweet_list,name='tweet_list'),
     path('create/',views.tweet_create,name='tweet_create'),
     path('<int:tweet_id>/edit/',views.tweet_edit,name='tweet_edit'),
     path('<int:tweet_id>/delete/',views.tweet_delete,name='tweet_delete'),
     path('register/', views.register,name='register'),
   
]

