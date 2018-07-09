from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board


# 인증보안처리
from user.models import User

def deleteform(request):

    id = request.GET.get('id',False)
    board_list = Board.objects.filter(id=id)
    board = board_list[0]

    print('board1231',board)
    context = {'board': board }
    return render(request,'board/deleteform.html',context)

def delete(request):
    id = request.POST['id'] # name = id로 들어왓으므로
    # if()
    print('id',id)
    password = request.POST['password'] # html에서 input으로 입력한 password
    #print('password : ', request.POST['password'])
    print(request.session['authuser']['password'])
    if password == request.session['authuser']['password']:
        Board.objects.filter(id=id).delete()
        return HttpResponseRedirect('/board')
    else:
        return HttpResponseRedirect('/board')


def writeform(request):
    print(request.session['authuser'])
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/joinform')# 로그인 안됫으면 회원가입 폼으로간다.


def list(request):

    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    print('board_list:', board_list)
    print('board123: ',board_list)
    return render(request,'board/list.html',context)


def modify(request):
    id = request.GET.get('id', False)
    board_list = Board.objects.filter(id=id) # filter방식으로 줬으므로 pk에 해당하는 row 여러개를 가져와서 쿼리셋 리스트에 담는다.
    board = board_list[0]
    context = { 'board':board }

    return render(request,'board/modify.html',context)

def update(request):
    #
    # if 'id' in request.GET:
    id = request.POST['id']
    print(id)
    board = Board.objects.get(id=id)# get방식으로 줬으므로 pk에 해당하는 row 하나만가져온다
    board.title = request.POST['title']
    board.content = request.POST['content']
    print(board.title)
    print(board.content)
    board.save()

    return HttpResponseRedirect('/board')
    # if 'title' in request.POST:
    #     Board.objects.filter(title=)
    # print('인영아:',request.POST['title'])
    # print('인녕아:',request.POST.get('title',False))
    # print('이녕: ',request.POST.get('title',False))
    # # board_list.content = request.POST.get('content',False)
    # # print('인영아:',board_list.title)

def hit_update(board):
    board.hit += 1
    board.save()

def view(request):
    # board_list = Board.objects.GET.get(id = request.POST['id'])
    id = request.GET.get('id',False)
    board_list = Board.objects.filter(id=id) # mysql에서 글번호만을 filter함
    board = board_list[0]
    hit_update(board) # 조회수 올리는 함수 hit_update호출
    context = { 'board' : board }
    print(board.title)
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

    board = Board() # POST방식으로 가져온 값을 DB에 새롭게 입력한 값을 넣는다
    #user = User()
    board.title=request.POST['title']
    board.content=request.POST['content']

    # title과 content는 write.html에서 작성하는 것이므로 user_id만 가져오면된다.
    board.user_id = request.session['authuser']['id']# user의 forienkey로 id를 가져온다.
    # board.name = request.session['authuser']['name'] # user앱의 model에서 name을 가져옴 name이 forienkey이므로
    # # print('request.session:',type(request.session['authuser']['name']))
    # print(type(board.name),'board.user.name : ' ,board.name) # mysql의 db에 있는 user name 정보를 가져다준다.
    board.save()

    return HttpResponseRedirect('/board')

