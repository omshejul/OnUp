from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('page404', views.page404, name="page404"),
    path('page500', views.page500, name="page500"),
    path('charts', views.charts, name="charts"),
    path('tables', views.tables, name="tables"),
    path('login', views.login, name="login"),
    path('password', views.password, name="password"),
    path('register', views.register, name="register"),
    # path('add',views.add,name='add')
]

 