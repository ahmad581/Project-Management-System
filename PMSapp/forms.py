from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import PasswordInput, TextInput, Textarea, DateInput, DateField, ChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Project, Task

# Register Form 
class RegisterUserForm(UserCreationForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(label = "UserName", widget=TextInput())
    # email = forms.CharField(label = "Email", widget=TextInput())
    password1 = forms.CharField(label = "Password", widget=PasswordInput())
    password2 = forms.CharField(label = "Password-Confirmatin", widget=PasswordInput())
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Add Bootstrap classes to individual fields
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('password1', css_class='form-control mb-3'),
            Field('password2', css_class='form-control mb-3')
        )

# LogIn Form
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label = "User Name", widget=TextInput())
    password = forms.CharField(label = "Password", widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        # Add Bootstrap classes to individual fields
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control mb-3')
        )

# Creat A New Project 
class CreateNewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_date', 'end_date', 'employees']

        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        
# Update A Project 
class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_date', 'end_date', 'employees']

        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'employees': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
        }

# Creat A New Task 
class CreateNewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'employees', 'project', 'task_number']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'name':'body', 'rows':4, 'cols':5, 'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'project': forms.HiddenInput(),
            'task_number': forms.HiddenInput()
        }
        
# Update A Task 
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'employees']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'name':'body', 'rows':4, 'cols':5, 'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control'})
        }