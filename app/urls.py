from django.urls import path

from . import views

urlpatterns = [
    path('<ticker>', views.company_basic, name='company_basic'),
]