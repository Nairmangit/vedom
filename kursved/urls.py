from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('logg', views.logg, name = 'logg'),
    path('loggout', views.loggout, name = 'loggout'),
    path('vedomid/<ved_id>', views.vedomid, name = 'vedomid'),
    path('save', views.save, name = 'save'),
]