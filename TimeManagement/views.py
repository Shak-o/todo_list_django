from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TaskListView(ListView):
    model = Task
    template_name = 'TimeManagement/home.html'
    context_object_name = 'task'
    ordering = ['-created_date']

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    context_object_name = 'task'
    fields = ['name','worked_hours','date','day','assignee','category']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['name','worked_hours','date','day','assignee','category']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        else:
            return False
class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Task
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        else:
            return False
    success_url = '/home/'
class TaskDetailView(DetailView):
    model = Task

def about(request):
    return render(request,'TimeManagement/about.html')