from django.urls import path

from .views import OrderCreateView
from .views import OrderDeleteView
from .views import OrderItemCreateView
from .views import OrderItemDeleteView
from .views import OrderItemListView
from .views import OrderItemUpdateView
from .views import OrderListView
from .views import OrderUpdateView
from .views import OrderDetailView
from .views import OrderItemDetailView

urlpatterns = [
    path("orderitem/create/", OrderItemCreateView.as_view(), name="orderitem-create"),
    path("orderitem/list/", OrderItemListView.as_view(), name="orderitem-list"),
    path(
        "orderitem/update/<int:pk>/",
        OrderItemUpdateView.as_view(),
        name="orderitem-update",
    ),
    path(
        "orderitem/delete/<int:pk>/",
        OrderItemDeleteView.as_view(),
        name="orderitem-delete",
    ),
    path(
        "orderitem/detail/<int:pk>/",
        OrderItemDetailView.as_view(),
        name="orderitem-detail",
    ),
    path("order/create/", OrderCreateView.as_view(), name="order-create"),
    path("order/list/", OrderListView.as_view(), name="order-list"),
    path("order/update/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
    path("order/delete/<int:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    path(
        "order/detail/<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),
]
