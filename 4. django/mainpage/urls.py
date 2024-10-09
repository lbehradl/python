from django.urls import path
from .views import mainpage_view

urlpatterns = [
    path('', mainpage_view, name='mainpage'),
]
