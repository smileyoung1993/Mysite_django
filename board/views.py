from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# 인증보안처리

def writeform(request):

    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')# 로그인 안됫으면 회원가입 폼으로간다.

