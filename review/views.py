from django.http import HttpResponse


def index(request):
    return HttpResponse("리뷰페이지입니다.")