from django.urls import path
from .views import userinfo_with_orders, user_orders

urlpatterns = [
    path('userinfo/', userinfo_with_orders, name='userinfo_with_orders'),
    path('orders/<str:id>/', user_orders, name='user_orders'), 
]
