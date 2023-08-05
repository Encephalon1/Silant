from django.urls import path, include
from .views import *


urlpatterns = [
    path('', UnauthorizedView.as_view(), name='unauthorised'),
    path('search/', SearchCarResultView.as_view(), name='search_results'),
    path('cars/', main, name='main'),
    path('cars/<str:pk>', CarDetail.as_view(), name='single_car'),
    path('cars/<str:pk>/maintenance', maintenance, name='maintenance'),
    path('cars/<str:pk>/reclamation', reclamation, name='reclamation'),
]
