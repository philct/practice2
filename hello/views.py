from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html', {
        'message': 'Hello, world!'
    })

def person(request, name):
    return render(request, 'hello/person.html', {
        'name': name.capitalize(),})