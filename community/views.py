from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from community.models import Board
from django.urls import reverse
from django.utils import timezone
from community.forms import BoardForm
from community.models import *


# Create your views here.
# 글 목록
def index(request):
    boards = {'boards': Board.objects.order_by('-created_date')}
    return render(request, 'community/board_list.html', boards)

 # # 입력 파라미터
 #    page = request.GET.get('page', '1')  # 페이지
 #
 #    # 조회
 #    review_list = Review.objects.order_by('-create_date')
 #
 #    # 페이징처리
 #    paginator = Paginator(review_list, 10)  # 페이지당 10개씩 보여주기
 #    page_obj = paginator.get_page(page)
 #
 #    context = {'review_list': page_obj}
 #    return render(request, 'review/review_list.html', context)


# 글 작성
def board_post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('community:index')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'community/board_form.html', context)

# 글 상세보기
def board_detail(request, post_id):
    board = get_object_or_404(Board, id=post_id)

    board_after = get_object_or_404(Board, id=post_id+1)
    board_before= get_object_or_404(Board, id=post_id-1)
    context = {
        'board':board,
        'board_after':board_after,
        'board_before':board_before,
    }
    return render(request, 'community/board_detail.html', context)


# 글 삭제
def board_delete(request, post_id):
    board = Board.objects.get(id=post_id)
    board.delete()
    messages.success(request, "삭제되었습니다.")
    return redirect('community:index')


# 글 수정
def board_modify(request, post_id):
    board = get_object_or_404(Board, id=post_id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.modify_date = timezone.now()
            board.save()
            return redirect('community:detail', post_id=post_id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'community/board_modify.html', context)
