from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterUserForm, LoginUserForm, CreateNewProjectForm, UpdateProjectForm, CreateNewTaskForm, UpdateTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Project, Task

# Create your views here.

def home(request):
    return render(request, 'PMSapp/index.html')

# Register 
def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    context = {'RegisterForm': form}
    return render(request, 'PMSapp/register.html', context = context)

# Log In 
def login(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('dashboard')
    context = {'LoginForm': form}
    return render(request, 'PMSapp/login.html', context = context)

# Dashboard 
@login_required(login_url='login')
def dashboard(request):
    projects = Project.objects.all()
    # projects = Project.objects.filter(employees=request.user)
    context = {'projects': projects}
    return render(request, 'PMSapp/dashboard.html', context=context)

# Create A New Project 
@login_required(login_url='login')
def create_project(request):
    form = CreateNewProjectForm()

    if request.method == 'POST':
        form = CreateNewProjectForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('dashboard')
    context = {'CreateProjectsForm': form}
    return render(request, 'PMSapp/create-project.html', context=context)

# show a specific project 
def project(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(project=project)
    context = {'project': project, 'tasks': tasks}
    return render(request, 'PMSapp/project.html', context=context)

# Update a Project 
@login_required(login_url='login')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = UpdateProjectForm(instance=project)

    if request.method == 'POST':
        form = UpdateProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            
            return redirect('project', pk=pk)
    context = {'UpadteProjectsForm': form, 'project': project}
    return render(request, 'PMSapp/update-project.html', context=context)

# Delete A Project 
@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('dashboard')

# Create New Task 
@login_required(login_url='login')
def create_task(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateNewTaskForm(initial={'project': project})

    if request.method == 'POST':
        form = CreateNewTaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.project = project
            task.save()
            return redirect('project', pk=pk)
        
    context = {'CreateTaskForm': form, 'project': project}
    return render(request, 'PMSapp/create-task.html', context=context)
    

# Show Specific Task 
@login_required(login_url='login')
def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'PMSapp/task.html', context=context)

# Update Task 
@login_required(login_url='login')
def update_task(request, project_pk, pk):
    project = Project.objects.get(id=project_pk)
    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(initial={'project': project}, instance=task)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)

        if form.is_valid():
            # task = 
            form.save()
            # task.project = project
            # task.save()
            return redirect('project', pk=project_pk)
        
    context = {'UpdatTaskForm': form, 'project': project}
    return render(request, 'PMSapp/update-task.html', context=context)

# Finish Task 
@login_required(login_url='login')
def finish_task(request, pk):
    task = Task.objects.get(id=pk)

    if task.status == True:
        task.status = False

    else:
        task.status = True

    task.save()
    return redirect('dashboard')

# Delete Task 
@login_required(login_url='login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('dashboard')

#  User logout
def logout(request):

    auth.logout(request)

    # messages.success(request, "Logout success!")

    return redirect("login")
