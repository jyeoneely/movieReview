from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def master(request):
    return render(request, 'master/master.html')