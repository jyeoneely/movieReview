from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from review.models import Review
from review.forms import ReviewForm
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 리뷰홈(목록) 구현
def index(request) :
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    review_list = Review.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'review_list': page_obj}
    return render(request, 'review/review_list.html', context)

    # review_list = Review.objects.order_by('-create_date')   # -create_date 오류잡기
    # context = {'review_list': review_list}
    # return render(request, 'review/review_list.html', context)

# 리뷰등록 구현
# @login_required(login_url='common:login')
def reviewCreate(request) :
    if request.method == 'POST':
        # if not request.user.is_authenticated:
        #     return redirect('accounts:login') 로그인 후 리뷰등록
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now()
            # review.author = request.user              # 회원가입 유저 변수명 받아오기
            review.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/review_form.html', context)

# 상세리뷰 구현
def reviewDetail(request,review_id) :
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'review/review_detail.html', context)

# 유저상세리뷰 구현
def reviewUserDetail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'review/review_userdetail.html', context)

# 리뷰 수정 구현
# @login_required(login_url='common:login')
def reviewModify(request,review_id) :
    review = get_object_or_404(Review, pk=review_id)

    #if request.user != review.author:
    #    messages.error(request, '수정권한이 없습니다')
    #    return redirect('review:detail', review_id=review.id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
           review = form.save(commit=False)
           review.modify_date = timezone.now()  # 수정일시 저장 재확인
           review.save()
           return redirect('review:review_detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'review/review_form.html', context)

# user detail delete 구현
# @login_required(login_url='common:login')
def reviewDelete(request, review_id) :
    review = get_object_or_404(Review, pk=review_id)
    #if request.user != review.author:
    #    messages.error(request, '삭제권한이 없습니다')
    #    return redirect('review:detail', review_id=review.id)
    review.delete()
    return redirect('review:index')

# like 구현
#@login_required(login_url='common:login')
def like_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    #if request.user == review.author:
    #    messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    #else:
    review.like_review += 1
    # review.like_review = review.like_review(request) + 1  : 가능
    # review.like_review.add(request) : 점프투장고ver
    review.save()
    return redirect('review:review_detail', review_id=review.id)

# unlike 구현
# @login_required(login_url='common:login')
def unlike_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    #if request.user == review.author:
    #    messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    #else:
    review.unlike_review += 1
    review.save()
    return redirect('review:review_detail', review_id=review.id)



