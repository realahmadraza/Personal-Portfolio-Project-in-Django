from django.urls import path
from portfolio_projects import views

urlpatterns = [
    path('', views.project_index, name= 'project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
