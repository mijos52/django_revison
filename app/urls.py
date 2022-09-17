from django.urls import path
from . views import customer_detail,login,signup,get_users,create_users

urlpatterns = [
    path('signup', signup),
    path('login', login),
    path('get_user', get_users),
    path('create_user', create_users),
    path('customers/<int:pk>', customer_detail),
]

