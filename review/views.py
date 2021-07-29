from django.http import HttpResponse
from .models import Review


def load_list(request) :
    review_list = Review.objects.order_by('-create_date')
    context = {'review_list': review_list}
    return render(request, 'review/question_list.html', context)

def reviewCreate(request) :
    return HttpResponse("리뷰등록페이지입니다.")

def reviewModify(request) :
    return HttpResponse("리뷰수정페이지입니다.")

def reviewDelete(request) :
    return HttpResponse("리뷰삭제페이지입니다.")

def reviewDetail(request) :
    return HttpResponse("상세리뷰페이지입니다.")