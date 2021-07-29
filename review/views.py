from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse("안녕하세요 Review Page에 오신 걸 환영합니다! ")