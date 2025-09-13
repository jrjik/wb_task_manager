from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/complete/', views.complete_task, name='task-complete'),
]