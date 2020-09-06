from django import forms
from .models import Task

class TaskCreationForm():
    name=forms.TextInput()
    day=forms.TextInput()
    assignee = forms.TextInput()
    worked_hours = forms.TextInput()
    date= forms.DateField()

    class Meta:
        model = Task
        fields = ['name', 'comment', 'assignee', 'worked_hours', 'date', 'day']
