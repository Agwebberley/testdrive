from django.urls import reverse_lazy
from frame.base_views import BaseCreateView
from frame.base_views import BaseDeleteView
from frame.base_views import BaseDetailView
from frame.base_views import BaseListView
from frame.base_views import BaseUpdateView

from .models import Order
from .models import OrderItem

# Create your views here.


class OrderItemCreateView(BaseCreateView):
    model = OrderItem
    success_url = reverse_lazy("orderitem-list")


class OrderItemListView(BaseListView):
    model = OrderItem


class OrderItemUpdateView(BaseUpdateView):
    model = OrderItem
    success_url = reverse_lazy("orderitem-list")


class OrderItemDeleteView(BaseDeleteView):
    model = OrderItem
    success_url = reverse_lazy("orderitem-list")


class OrderItemDetailView(BaseDetailView):
    model = OrderItem


class OrderCreateView(BaseCreateView):
    model = Order
    success_url = reverse_lazy("order-list")


class OrderListView(BaseListView):
    model = Order


class OrderUpdateView(BaseUpdateView):
    model = Order
    success_url = reverse_lazy("order-list")


class OrderDeleteView(BaseDeleteView):
    model = Order
    success_url = reverse_lazy("order-list")


class OrderDetailView(BaseDetailView):
    model = Order
