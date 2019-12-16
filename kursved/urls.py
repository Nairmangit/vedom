from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('logg', views.logg, name = 'logg'),
    path('loggout', views.loggout, name = 'loggout'),
]