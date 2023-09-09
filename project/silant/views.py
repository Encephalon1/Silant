from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


class UnauthorizedView(ListView):
    model = Car
    template_name = 'unauthorized.html'
    context_object_name = 'cars'


class SearchCarResultView(ListView):
    model = Car
    template_name = 'SearchCarResult.html'

    def get_queryset(self):
        query = self.request.GET.get('search_car')
        object_list = Car.objects.filter(factory_car_num__exact=query)

        return object_list


@login_required(login_url='/accounts/login/')
def main(request):
    context = {
        'user_cars': Car.objects.filter(client=request.user)
    }
    return render(request, 'MainPage.html', context)


class CarDetail(DetailView, LoginRequiredMixin):
    model = Car
    template_name = 'Car.html'
    context_object_name = 'car_detail'
    login_url = '/accounts/login/'


@login_required(login_url='/accounts/login/')
def maintenance(request, pk):
    context = {
        'maintenances': Maintenance.objects.filter(car=pk)
    }
    return render(request, 'Maintenance.html', context)


@login_required(login_url='/accounts/login/')
def reclamation(request, pk):
    context = {
        'reclamations': Reclamation.objects.filter(car=pk)
    }
    return render(request, 'Reclamation.html', context)


class MaintenanceCreate(PermissionRequiredMixin, CreateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'maintenance_edit.html'
    permission_required = 'silant.add_maintenance'


class ReclamationCreate(PermissionRequiredMixin, CreateView):
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation_edit.html'
    permission_required = 'silant.add_reclamation'


class MaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'maintenance_edit.html'
    permission_required = 'silant.change_maintenance'


class ReclamationUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation_edit.html'
    permission_required = 'silant.change_reclamation'
