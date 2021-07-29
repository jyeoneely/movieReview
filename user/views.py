from django.http import HttpResponse


def index(request):
    return HttpResponse("사용자페이지입니다.")