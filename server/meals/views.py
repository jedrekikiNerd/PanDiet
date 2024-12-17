from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Meal
from .serializers import MealSerializer
from common.permission_classes import IsAdminOrDietitian, IsAdminOrDietitianOrClient


class MealViewSet(ModelViewSet):
    """
    API endpoint for Meal table (add, edit, remove, list).
    """
    serializer_class = MealSerializer
    permission_classes = [IsAdminOrDietitianOrClient]

    # Filters and search
    filter_backends = [
        DjangoFilterBackend,  # Handle filter
        SearchFilter,         # Handle search
        OrderingFilter        # Handle sort
    ]

    # Filter
    filterset_fields = ['author', 'visibility', 'products', 'tags']

    # Search
    search_fields = ['name', 'mass', 'author', 'products', 'tags']

    # Sort
    ordering_fields = ['name', 'mass']

    def get_queryset(self):
        user = self.request.user

        # Admin sees all objects
        if user.role == 'admin':
            return Meal.objects.all()

        # Dietitian sees only public meals or their own meals
        if user.role == 'dietitian':
            return Meal.objects.filter(
                Q(author=user) | Q(visibility='public')
            )

        if user.role == 'client':
            return Meal.objects.filter(
                Q(id__in=user.diet_plan.meals.values_list('id', flat=True))
            )

        # In other cases, no access
        return Meal.objects.none()

    def perform_update(self, serializer):
        # Check if the user has permission to edit the object
        obj = self.get_object()
        if obj.author != self.request.user and self.request.user.role != 'admin':
            raise PermissionDenied("You don't have permission to edit this object.")
        serializer.save()

    def perform_destroy(self, instance):
        # Check if the user has permission to delete the object
        obj = self.get_object()
        if obj.author != self.request.user and self.request.user.role != 'admin':
            raise PermissionDenied("You don't have permission to delete this object.")
        instance.delete()
