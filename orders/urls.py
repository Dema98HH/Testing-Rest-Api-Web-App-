from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderTestView.as_view(), name='orders_test'),
    path('create', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:order_id>', views.UpdateOrderStatus.as_view(), name='order_status_update')
]