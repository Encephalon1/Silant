from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', UnauthorizedView.as_view(), name='unauthorised'),
    path('search/', SearchCarResultView.as_view(), name='search_results'),
    path('cars/', main, name='main'),
    path('cars/<str:pk>', CarDetail.as_view(), name='single_car'),
    path('cars/<str:pk>/maintenance', maintenance, name='maintenance'),
    path('cars/<str:pk>/reclamation', reclamation, name='reclamation'),
    path('cars/maintenance/create', MaintenanceCreate.as_view(), name='maintenance_create'),
    path('cars/reclamation/create', ReclamationCreate.as_view(), name='reclamation_create'),
    path('cars/maintenance/<int:pk>/update', MaintenanceUpdate.as_view(), name='maintenance_update'),
    path('cars/reclamation/<int:pk>/update', ReclamationUpdate.as_view(), name='reclamation_update'),
]
