from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('variable', views.variable, name="variable"),
   path('random', views.randomnumber, name="random "),
   path('loop', views.loop_example, name='loop'),
   path('fizzbuzz', views.fizzbuzz, name='fizzbuzz'),
]