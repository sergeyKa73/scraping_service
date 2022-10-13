from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Ivan'
    data_context = {'date': date, 'name': name}
    return render(request, 'home.html', data_context)