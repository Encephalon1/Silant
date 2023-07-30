from django.urls import path
from .views import *


urlpatterns = [
    path('', UnauthorizedView.as_view(), name='unauthorised'),
    path('search/', SearchCarResultView.as_view(), name='search_results'),
    path('cars/', main, name='main'),
    path('cars/<int:pk>', CarDetail.as_view(), name='single_car'),
    path('cars/<int:pk>/maintenance', MaintenanceDetail.as_view(), name='single_maintenance'),
    path('cars/<int:pk>/reclamation', ReclamationDetail.as_view(), name='single_reclamation'),
]
