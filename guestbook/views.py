from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect
# Create your views here.
# templates를 전체 directory로 만든다.
# Where 절은 fillter()

def deleteform(request):
    id = request.GET.get('id',False)
    content = {'id': id }
    return render(request,'guestbook/deleteform.html',content)

def delete(request):
      # guestbook = Guestbook()
    # print(type(guestbook_id),guestbook_id)
    # print(type(guestbook_password),guestbook_password)

    id = request.POST['id']
    password = request.POST['password']
    # Guesbook.save()
    Guestbook.objects.filter(id=id).filter(password=password).delete()

    return HttpResponseRedirect('/guestbook')



def index(request):

    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list':guestbook_list}

    return render(request, 'guestbook/list.html',context)


def guest_lst(request):

    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}
    return render(request,'guestbook/guestbook_L.html',context)

def add(request):

    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save() # db에 import

    return HttpResponseRedirect('/guestbook') # 다시 방명록목록으로 가게 함

