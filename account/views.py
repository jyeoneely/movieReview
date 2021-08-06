from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.contrib import auth

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'account/index.html')
    else:
        return redirect('account:login')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'account/login.html', {'error' : '아이디 또는 패스워드를 확인해주세요.'})
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'account/login.html', context)


