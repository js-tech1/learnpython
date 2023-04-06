from django import views
from django .urls import path
from app import views
urlpatterns = [
    path('',views.ShowLoginForm),
]
