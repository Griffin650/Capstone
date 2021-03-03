from django.urls import path

from . import views

app_name = 'gpu'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.CardView.as_view(), name='gpu_card'),
]
