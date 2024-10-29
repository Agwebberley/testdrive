from django.urls import reverse_lazy
from frame.base_views import BaseCreateView
from frame.base_views import BaseDeleteView
from frame.base_views import BaseDetailView
from frame.base_views import BaseListView
from frame.base_views import BaseUpdateView

from .models import Part

# Create your views here.


class PartCreateView(BaseCreateView):
    model = Part
    success_url = reverse_lazy("part-list")


class PartListView(BaseListView):
    model = Part


class PartUpdateView(BaseUpdateView):
    model = Part
    success_url = reverse_lazy("part-list")


class PartDeleteView(BaseDeleteView):
    model = Part
    success_url = reverse_lazy("part-list")


class PartDetailView(BaseDetailView):
    model = Part
