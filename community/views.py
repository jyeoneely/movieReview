from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from community.models import Board
from django.urls import reverse
from django.utils import timezone
from community.forms import BoardForm
from community.models import *
from django.db.models import Q


# Create your views here.
# 글 목록
def index(request):
    # boards = {'boards': Board.objects.order_by('-created_date')}
    # return render(request, 'community/board_list.html', boards)

    page = request.GET.get('page', '1')
    # 조회
    board_list = Board.objects.order_by('-created_date')

    # 페이징처리
    paginator = Paginator(board_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # max_index = len(paginator.page_range)
    # page = self.request.Get.get('page')
    # current_page = int(page) if page else 1
    #
    # start_index =  int((current_page-1) / page_numbers_range) * page_number

    context = {'board_list': page_obj}
    return render(request, 'community/board_list.html', context)


# 글 작성
def board_post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer_id = 1
            board.created_date = timezone.now()
            board.save()
            return redirect('community:index')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'community/board_form.html', context)

# 글 상세보기
def board_detail(request, post_id):
    boardPerPage = Board.objects.order_by('-created_date')

    index = -1
    board_before = None
    board_after = None

    for b in boardPerPage:
        index += 1
        if b.id == post_id:
            board = b
            break
    if index > 0:
        board_before = boardPerPage[index - 1]
    if index < len(boardPerPage)-1:
        board_after = boardPerPage[index + 1]

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
            board.modified_date = timezone.now()
            board.save()
            return redirect('community:detail', post_id=post_id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'community/board_modify.html', context)


# 글 검색기능

#파일 업로드

#조회수
