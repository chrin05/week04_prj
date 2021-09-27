from django.urls import path
from . import views

urlpatterns = [
    path('about_me4/', views.about_me4),
    path('', views.landing4),
]