from django.urls import path

from .views import PartCreateView
from .views import PartDeleteView
from .views import PartListView
from .views import PartUpdateView

urlpatterns = [
    path("part/create/", PartCreateView.as_view(), name="part-create"),
    path("part/list/", PartListView.as_view(), name="part-list"),
    path("part/update/<int:pk>/", PartUpdateView.as_view(), name="part-update"),
    path("part/delete/<int:pk>/", PartDeleteView.as_view(), name="part-delete"),
]
