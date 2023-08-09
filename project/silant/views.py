from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
