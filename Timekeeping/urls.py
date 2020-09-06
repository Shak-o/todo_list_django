"""Timekeeping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as usviews
from TimeManagement import views as timeviews

urlpatterns = [
    path('reg/',usviews.registration, name='keep_reg'),
    path('about/',timeviews.about, name='keep_about'),
    path('reg/err',usviews.regerr, name='keep_reg_err'),
    path('logout/', usviews.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/login/',usviews.login, name='login'),
    path('',usviews.login, name='login'),
    path('home/',timeviews.TaskListView.as_view(), name='keep_home'),
    path('error/',usviews.error, name="log_error"),
    path('task/new', timeviews.TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', timeviews.TaskUpdateView.as_view(), name='update'),
    path('task/<int:pk>/delete/', timeviews.TaskDeleteView.as_view(), name='delete'),
]
