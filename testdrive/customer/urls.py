from django.urls import path

from .views import CustomerCreateView
from .views import CustomerDeleteView
from .views import CustomerListView
from .views import CustomerUpdateView

urlpatterns = [
    path("customer/create/", CustomerCreateView.as_view(), name="customer-create"),
    path("customer/list/", CustomerListView.as_view(), name="customer-list"),
    path(
        "customer/update/<int:pk>/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "customer/delete/<int:pk>/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
]
