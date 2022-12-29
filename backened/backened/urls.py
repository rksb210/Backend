"""backened URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo-list/', views.todolist),
    path('todo-detail/<int:pk>/', views.tododetail),
    path('todo-create/', views.todocreate),
    path('todo-update/<int:pk>/', views.todoupdate),
    path('todo-delete/<int:pk>/', views.tododelete),



    # path('todo-list/', views.todolist.as_view()),
    # path('todo-retrieve/<int:pk>/', views.todoretrieve.as_view()),
    # path('todo-create/', views.todocreate.as_view()),
    # path('todo-update/<int:pk>/', views.todoupdate.as_view()),
    # path('todo-destroy/<int:pk>/', views.tododestroy.as_view()),
    path('auth/',include('rest_framework.urls'))

    
]
