"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import user.views as user_view
import main.views as main_view
import guestbook.views as guestbook_view
import board.views as board_view


urlpatterns = [

    path('',main_view.index),

    # guestbook
    path('guestbook/', guestbook_view.index),
    path('guestbook/guest_lst',guestbook_view.guest_lst),
    path('guestbook/add',guestbook_view.add),
    path('guestbook/deleteform', guestbook_view.deleteform),
    path('guestbook/delete', guestbook_view.delete),

    # url에서 포스트방식으로 보내는 방식은 /를 붙이면 안된다.
    path('user/joinform/',user_view.joinform),
    path('user/join', user_view.join),
    path('user/joinsuccess/', user_view.joinsuccess),
    path('user/loginform/', user_view.loginform),
    path('user/login', user_view.login),
    path('user/logout',user_view.logout),

    # board
    path('board/',board_view.list),
    path('board/modify',board_view.modify),
    path('board/view',board_view.view),
    path('board/write',board_view.write),
    path('board/add',board_view.add),

    path('admin/', admin.site.urls),  # view 이름이 site


]


