from django.urls import path
from . views import customer_detail,customers

urlpatterns = [
    # path("", views.),
    # path("signup/", sign_up, name="signup"),
    path('customers', customers),
    path('customers/<int:pk>', customer_detail),
]

