from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from community.models import Board
from django.urls import reverse
from django.utils import timezone
from community.forms import BoardForm
from community.models import *

# Create your views here.
#글 목록
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'community/board_list.html', boards)

#글 작성
def board_post(request):
    if request.method == "POST":
        form = BoardForm(request.post)
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.created_date = timezone.now()
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'community/board_post.html', )

#글 상세보기
def board_detail(request, id):
    board = get_object_or_404(Board, pk=id)
    context = {'board': board}
    return render(request, 'community/board_detail.html', context)

#글 삭제
def board_delete(request, id):
    pass

#글 수정
def board_modify(request,id):
    pass
