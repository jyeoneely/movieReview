from django.shortcuts import render
from .models import Board
from .forms import BaseBoard
from django.views import generic



def boardView(request):
     template_name = 'community/community.html'
     board_object = Board.objects.order_by('-write_date')
     context = {'board_object': board_object}
     return render(request, template_name, context)

class DetailView(generic.DetailView):
    model = Board

def writePageView(request):
    template_name = 'community/write_page.html'
    form = BaseBoard()
    context = {'form': form}
    return render(request, template_name, context)


