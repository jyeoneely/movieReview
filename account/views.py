from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'account/index.html')
    else:
        return redirect('account:login')

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('master:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)

