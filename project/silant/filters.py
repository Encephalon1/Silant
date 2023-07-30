from django_filters import FilterSet
from .models import Car, Maintenance, Reclamation


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'technique_model__name': ['iexact'],
            'engine_model__name': ['iexact'],
            'transmission_model__name': ['iexact'],
            'drive_axle_model__name': ['iexact'],
            'steerable_bridge_model__name': ['iexact']
        }


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            'kind_of_maintenance__name': ['icontains'],
            'car': ['exact'],
            'service_company__name': ['iexact']
        }


class ReclamationFilter(FilterSet):
    class Meta:
        model = Reclamation
        fields = {
            'failure_node__name': ['icontains'],
            'recovery_method__name': ['icontains'],
            'service_company__name': ['iexact']
        }
