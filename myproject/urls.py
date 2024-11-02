"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Todoapp import views
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/create', views.create_todo, name='create_todo'),
    path('todo/complete/<int:todo_id>', views.complete_todo, name='complete_todo'),
    path('todo/Delete/<int:todo_id>', views.Delete_todo, name='Delete_todo'),
    path('todo/update/<int:todo_id>', views.update_todo, name='update_todo'),
    path('admin/', admin.site.urls),
]
