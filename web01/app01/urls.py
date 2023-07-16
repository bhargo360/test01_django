from django.urls import path
from . import views

urlpatterns = [
    path('app01/', views.app01, name='app01'),
]