from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_core, name='all_core'),
]
