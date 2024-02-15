from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-project', views.create_project, name='create-project'),
    path('project/<int:pk>', views.project, name='project'),
    path('update-project/<int:pk>', views.update_project, name='update-project'),
    path('delete-project/<int:pk>', views.delete_project, name='delete-project'),
    path('create-task/<int:pk>', views.create_task, name='create-task'),
    path('task/<int:pk>', views.task, name='task'),
    path('update-task/<int:project_pk>/<int:pk>', views.update_task, name='update-task'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('finish-task/<int:pk>', views.finish_task, name='finish-task'),
    path('logout', views.logout, name="logout"),
]