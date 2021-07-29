from django.http import HttpResponse


def index(request):
    return HttpResponse("관리자페이지입니다.")