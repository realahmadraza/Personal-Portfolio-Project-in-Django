from django.urls import path
from Portfolio_pages import views

urlpatterns = [
    path("", views.home, name='home'),
]