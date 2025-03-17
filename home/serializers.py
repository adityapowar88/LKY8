from rest_framework import serializers
from .models import UserInfo, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)  # Fetch related orders

    class Meta:
        model = UserInfo
        fields = '__all__'
