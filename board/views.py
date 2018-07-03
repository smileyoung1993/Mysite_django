from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board
# Create your views here.

# 인증보안처리

def writeform(request):

    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')# 로그인 안됫으면 회원가입 폼으로간다.
    else:
        return render(request,'board/write.html')

def list(request):

    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    print('board_list:', request.GET.get('board_list',False))
    return render(request,'board/list.html',context)


def modify(request):
    return render(request,'board/modify.html')

def view(request):
    return render(request,'board/view.html')

def write(request):
    id = 
    return render(request,'board/write.html')

def add(request): # action ='' 에서 request가 들어온다

    board = Board()
    board.title=request.POST['title']
    board.content=request.POST['content']

    print(board.content)
    # title과 content는 write.html에서 작성하는 것이므로 user_id만 가져오면된다.
    board.hit=1
    board.user_id=request.session['authuser']['name'] # user앱의 model에서 name을 가져옴
    print(type(board.user_id),board.user_id) # mysql의 db에 있는 user name 정보를 가져다준다.
    board.save()

    return HttpResponseRedirect('/board')

