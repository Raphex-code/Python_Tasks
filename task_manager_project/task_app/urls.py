from django.urls import path
from . import views

urlpatterns = [
  path('', views.task_list_view, name='task_list'),
  path('update/<int:pk>/', views.update_task_view, name='update_task'),
  path('delete/<int:pk>/', views.delete_task_view, name='delete_task'),
  path('complete/<int:pk>/', views.toggle_complete_view, name='toggle_complete'),
]