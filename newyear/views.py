from django.shortcuts import render
from datetime import datetime
# Create your views here.

current_month = datetime.now().month
current_date = datetime.now().day

def index(request):
    return render(request, 'newyear/index.html',
                   {'current_date': current_date, 'current_month': current_month})
