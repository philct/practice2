from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task', max_length=100)
    priority = forms.IntegerField(label='priority', min_value=1, max_value=10)

tasks = ['Buy groceries', 'Walk the dog', 'Finish homework']
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })