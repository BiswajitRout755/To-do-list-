from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name='base/login.html' #loginview model only supports this template name 
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user = True
    success_url=reverse_lazy('tasks')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request.user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self,).get(*args, **kwargs)
    
def logout_view(request):
    logout(request)
    return redirect('login')






# Create your views here.
class TaskList( LoginRequiredMixin,ListView): #Listview consists of a templates and a query set means all the tables and schemas in the database..and this renders all the mdoels we have created earlier and we can redner that to the web page.
    model= Task
    context_object_name= 'tasks'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']= context['tasks'].filter(
                title__startswith=search_input)
            
        context['search-input']= search_input
        return context

class TaskDetail(LoginRequiredMixin,DetailView):  #gives details about the page you desired forr...
    model=Task
    context_object_name='task'
    template_name= 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView): #this class will helps in creating the task..
    model=Task
    #we will create the model form and the modelform will create titles, description everything in the form format..
    fields =['title', 'description', 'complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):  #this UpdateView class also looks for the model name_form (task_form.html) templates..
    model=Task
    fields=['title', 'description', 'complete']
    success_url=reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin,DeleteView): #automatically deletes the task from the model
    model=Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')


  
