from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


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


def main(request):
    context = {
        'user_cars': Car.objects.filter(client=request.user)
    }
    return render(request, 'MainPage.html', context)


class CarDetail(DetailView):
    model = Car
    template_name = 'Car.html'
    context_object_name = 'car_detail'


class MaintenanceDetail(DetailView):
    model = Maintenance
    template_name = 'Maintenance.html'
    context_object_name = 'maintenance_detail'


class ReclamationDetail(DetailView):
    model = Reclamation
    template_name = 'Reclamation.html'
    context_object_name = 'reclamation_detail'
