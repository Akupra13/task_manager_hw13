from django.urls import path
from .views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    TaskStatsView,
    CategoryCreateView,
    SubTaskListCreateView,
    SubTaskRetrieveUpdateDestroyView
)
urlpatterns = [
    # задачи
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    # статистика задач
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    # категории
    path('categories/', CategoryCreateView.as_view(), name='category-create'),
    # подзадачи
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
]
