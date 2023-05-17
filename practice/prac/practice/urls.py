from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('new/<int:id>', new, name='new'),
    path('profi/<int:id>', profi, name='profi'),
    path('expert/<int:id>', expert, name='expert'),
    path('final', final, name='final')
]
