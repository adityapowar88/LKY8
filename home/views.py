from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserInfo, Order
from .serializers import UserInfoSerializer, OrderSerializer

@api_view(['POST'])
def userinfo_with_orders(request):
    serializer = UserInfoSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save user info
        
        # Fetch all orders for this user
        orders = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(orders, many=True)
        
        return Response({
            "user_info": serializer.data,
            "orders": order_serializer.data
        }, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def user_orders(request, id):
    user = get_object_or_404(UserInfo, id=id)
    orders = Order.objects.filter(user=user)
    order_serializer = OrderSerializer(orders, many=True)
    
    return Response({
        "user_info": UserInfoSerializer(user).data,
        "orders": order_serializer.data
    })
