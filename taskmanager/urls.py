from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
# Простой API-ответ для корневого пути
class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Task Manager API!"})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', RootView.as_view(), name='root'),
]
