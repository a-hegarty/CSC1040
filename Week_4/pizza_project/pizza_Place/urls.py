from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('home', views.userhome, name='home'),
   path('signup', views.create_user, name='createuser'),
   path('login', views.login, name='login'),
   path('order', views.order, name='order'),
   path('payment', views.payment, name='payment'),
   path('userhome', views.userhome, name='userhome')
]