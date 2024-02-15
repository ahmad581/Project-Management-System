from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.

# Employee Model 
# class Employee(AbstractUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=30)
#     email = models.EmailField(max_length=100)
#     department = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.first_name + " " + self.last_name 
    
# Project Model 
class Project(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(User)
    # tasks = models.ManyToManyField(Task)

    def __str__(self) -> str:
        return self.project_name

# Task Model 
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    employees = models.ManyToManyField(User)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_number = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title + ': ' + self.description 
    # + ', ENDS IN: ' + self.due_date

    def save(self, *args, **kwargs):
        if not self.id:
            last_task = Task.objects.filter(project = self.project).order_by('-task_number').first()

            if last_task:
                self.task_number = last_task.task_number + 1

        super().save(*args, **kwargs)


    
