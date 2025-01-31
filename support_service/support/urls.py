from django.urls import path
from .views import create_ticket


urlpatterns = [
    path('', create_ticket, name='create_ticket'),
]