from rest_framework import generics
from rest_framework import filters
from .models import Task, SubTask, Category
from rest_framework.response import Response
from .serializers import TaskSerializer, SubTaskSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# Пагинация
class TaskPagination(PageNumberPagination):
    page_size = 10


# Список и создание задач
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['status', 'deadline']  #по статусу и дедлайну
    search_fields = ['title', 'description']  #по названию и описанию
    ordering_fields = ['created_at']  #по дате создания
    ordering = ['created_at']


# Получение обновление удаление
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Статистика
class TaskStatsView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        task_count = Task.objects.count()
        return Response({"task_count": task_count})


# Список и создание подзадач
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    pagination_class = TaskPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['status', 'deadline']  #по статусу и дедлайну
    search_fields = ['title', 'description']  #по названию и описанию
    ordering_fields = ['created_at']  #по дате создания
    ordering = ['created_at']


# Получение обновление и удаление
class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer


# Создание категории
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
