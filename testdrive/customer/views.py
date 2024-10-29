from django.urls import reverse_lazy
from frame.base_views import BaseCreateView
from frame.base_views import BaseDeleteView
from frame.base_views import BaseDetailView
from frame.base_views import BaseListView
from frame.base_views import BaseUpdateView

from .models import Customer

# Create your views here.


class CustomerCreateView(BaseCreateView):
    model = Customer
    success_url = reverse_lazy("customer-list")


class CustomerListView(BaseListView):
    model = Customer


class CustomerUpdateView(BaseUpdateView):
    model = Customer
    success_url = reverse_lazy("customer-list")


class CustomerDeleteView(BaseDeleteView):
    model = Customer
    success_url = reverse_lazy("customer-list")


class CustomerDetailView(BaseDetailView):
    model = Customer
