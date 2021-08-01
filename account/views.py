from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.
def index(request) :
    return render(request, 'account/index.html')


def signup(request):
    """
    회원가입
    """
    if request.user.is_authenticated:   # 로그인 된 사용자의 경우 회원가입으로 이동하지 못하도록
        return redirect('index')
    if request.method == "POST":        # post로 요청이 들어올 경우 검증 후 index로 redirect
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserCreationForm()       # get으로 요청이 들어올 경우 form 호출
    return render(request, 'account/signup.html', {'form': form})


def profile(request, pk):
    """
    내 프로필
    """
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    return render(request, 'account/profile.html', {'user' : user})

