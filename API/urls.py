from django.urls import path
from . import views
urlpatterns = [
    path('them-dau/', views.APIThemDau.as_view()),
]