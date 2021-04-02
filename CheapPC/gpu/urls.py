from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'gpu'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('<int:pk>/', views.gpu_card, name='gpu_card'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
