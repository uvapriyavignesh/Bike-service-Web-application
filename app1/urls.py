from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home,name="index"),
    path('login/', LoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('dashboard/', views.dash,name="dashboard"),
    path('register/', views.register,name="register"),
    path('dashboard/service/', views.service,name="service"),
    path('dashboard/order/', views.myorder,name="order"),
    path('dashboard/service/booking/<str:ser>', views.bookingform,name="form"),

]
