from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board


# 인증보안처리
from user.models import User


def writeform(request):
    print(request.session['authuser'])
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/joinform')# 로그인 안됫으면 회원가입 폼으로간다.


def list(request):

    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    print('board_list:', request.GET.get('board_list',False))
    return render(request,'board/list.html',context)


def modify(request):
    return render(request,'board/modify.html')

def view(request):

    id = request.GET.get('id',False)
    context = { 'id': id }
    return render(request,'board/view.html',context)

# def viewform(request):
#
#     board_list = Board.objects.all().order_by('-regdate')
#     context = {'board_list': board_list}
#     print('board_list:', request.GET.get('board_list', False))
#     return render(request, 'board/view.html', context)

def write(request):

    # id = request.GET.get('id',False)
    # context = {'id':id }

    return render(request,'board/write.html')

def add(request): # action ='' 에서 request가 들어온다

    board = Board()
    #user = User()
    board.title=request.POST['title']
    board.content=request.POST['content']

    # title과 content는 write.html에서 작성하는 것이므로 user_id만 가져오면된다.
    board.hit=1
    board.user_id = request.session['authuser']['id']# user의 forienkey로 id를 가져온다.
    board.name = request.session['authuser']['name'] # user앱의 model에서 name을 가져옴 name이 forienkey이므로
    # print('request.session:',type(request.session['authuser']['name']))
    print(type(board.name),'board.user.name : ' ,board.name) # mysql의 db에 있는 user name 정보를 가져다준다.
    board.save()

    return HttpResponseRedirect('/board')

