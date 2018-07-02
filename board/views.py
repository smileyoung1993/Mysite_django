from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board
# Create your views here.

# 인증보안처리

def writeform(request):

    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')# 로그인 안됫으면 회원가입 폼으로간다.

def list(request):

    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}

    return render(request,'board/list.html',context)


def modify(request):

    return render(request,'board/modify.html')

def view(request):
    return render(request,'board/view.html')

def write(request):

    return render(request,'board/write.html')

