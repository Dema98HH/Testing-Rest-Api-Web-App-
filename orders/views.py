from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from .models import Order, User
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend




User = get_user_model()

class OrderTestView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class= serializers.OrderTestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'size', 'order_status', 'customer']


class OrderCreateListView(generics.GenericAPIView):

    serializer_class=serializers.OrderCreationSerializer

    permission_classes=[IsAuthenticated]


    @swagger_auto_schema(operation_summary="Create a new Order")
    def post(self, request):

        data=request.data

        serializer=self.serializer_class(data=data)



        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OrderDetailView(generics.GenericAPIView):

    serializer_class = serializers.OrderDetailsSerializer
    
    permission_classes=[IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(operation_summary="Change an Order")
    def put(self, request, order_id):
        data=request.data

        order = get_object_or_404(Order, pk=order_id)

        serializer=self.serializer_class(data=data, instance=order)


        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(operation_summary="Delete an Order")
    def delete(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)

        order.delete()
        
        return Response(data={"message":"Deleted!"}, status=status.HTTP_204_NO_CONTENT)




class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer

    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary="Update Orders Status")
    def put(self, request, order_id):
        
        order = get_object_or_404(Order, pk=order_id)


        data = request.data

        serializer = self.serializer_class(data=data, instance=order)


        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
