from django import forms
from .models import *


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'kind_of_maintenance',
            'running_time',
            'work_order',
            'car',
            'service_company'
        ]


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = [
            'running_time',
            'failure_node',
            'failure_description',
            'recovery_method',
            'used_spare_parts',
            'car',
            'service_company'
        ]
