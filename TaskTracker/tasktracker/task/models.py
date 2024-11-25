from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Archived', 'Archived')])

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    performer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15, choices=[('Grooming', 'Grooming'), ('In Progress', 'In Progress'), ('Dev', 'Dev'), ('Done', 'Done')])
    priority = models.CharField(max_length=6, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    tester = models.ForeignKey(User, related_name='task_tester', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
