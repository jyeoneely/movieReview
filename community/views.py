from django.http import HttpResponse


def index(request):
    return HttpResponse("자유게시판입니다")