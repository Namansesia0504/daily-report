from django.urls import path
from .views import register, login,get_all_users,get_user_data

 
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('users/', get_all_users, name='get-all-users'),
    path('user',get_user_data,name='user')
 
]