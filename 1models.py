from django.db import models


# категория для задач
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# модель задачи
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,
                              choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# модель подзадачи
class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,
                              choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
