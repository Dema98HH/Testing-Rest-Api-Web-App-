from email.policy import default
from .models import Order, User
from rest_framework import serializers


class OrderTestSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantiny = serializers.IntegerField()
    created = serializers.DateTimeField()


    class Meta:
        model=Order
        fields = ['id', 'size', 'order_status', 'quantiny', 'created', 'customer']



class OrderCreationSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantiny = serializers.IntegerField()
    created = serializers.DateTimeField()


    class Meta:
        model=Order
        fields = ['id', 'size', 'order_status', 'quantiny', 'created', 'customer']


class OrderDetailsSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantiny = serializers.IntegerField()
    created = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    class Meta:
        model=Order
        fields = ['id', 'size', 'order_status', 'quantiny', 'created', 'updated_at']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=20)

    class Meta:
        model = Order
        fields = ['order_status']