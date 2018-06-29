from django.contrib import admin
from guestbook.models import Guestbook
# Register your models here.
# makemigrations를 하기전에 admin으로 테이블을 등록해준다.
# makemigrations를 하면, guestbook의 model의 정보가 migrations디렉토리에 0001_initial.py가 생긴다.
# model이 바뀌면 무조껀 manage.py migrations를 해준다,
admin.site.register((Guestbook))

