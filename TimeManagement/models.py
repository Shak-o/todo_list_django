from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateField(blank=True, null=True)
    worked_hours = models.CharField(max_length=3)
    assignee = models.CharField(max_length=25)
    day = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('keep_home')