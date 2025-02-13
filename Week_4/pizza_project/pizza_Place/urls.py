from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('home', views.home, name='home'),
   path('signup', views.signup, name='signup'),
   path('login', views.login, name='login'),
   path('order', views.order, name='order'),
   path('payment', views.payment, name='payment'),
   path('userhome/<int:userid>', views.userhome, name='userhome'),
   path('logout', views.logout, name='logout'),
   path('vieworder', views.vieworder, name='vieworder')
]