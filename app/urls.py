from django.urls import path
from . views import customer_detail,customers,login,signup

urlpatterns = [
    path('signup', signup),
    path('login', login),
    path('customers', customers),
    path('customers/<int:pk>', customer_detail),
]

