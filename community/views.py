from django.contrib import messages
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
    boards = {'boards': Board.objects.all()}
    return render(request, 'community/board_list.html', boards)


# 글 작성
def board_post(request):
    if request.method == "POST":
        form = BoardForm(request.post)
        writer = request.POST['author']
        title = request.POST['title']
        content_type = request.POST['content_type']
        content = request.POST['content']
        board = Board(
            writer=writer,
            title=title,
            content_type=content_type,
            content=content)
        board.created_date = timezone.now()
        board.save()
        return redirect(reverse('index'))
    else:
        return render(request, 'community/board_post.html')


# 글 상세보기
def board_detail(request, post_id):
    try:
        board = Board.objects.get(pk=post_id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")

    board = get_object_or_404(Board, pk=post_id)

    return render(request, 'community/board_detail.html', {'board': board})


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
