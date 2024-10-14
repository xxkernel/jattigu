# exercise_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('training-plans/', views.training_plan_list, name='training_plan_list'),
    path('training-plans/<int:pk>/', views.training_plan_detail, name='training_plan_detail'),
    path('schedules/', views.schedule_list, name='schedule_list'),
]
