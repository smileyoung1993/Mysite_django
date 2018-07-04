from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):

    title = models.CharField(max_length= 200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)#값이없으면 디폴트값
    regdate = models.DateTimeField(auto_now= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)# 주키가 삭제되면 같이(모두가) 지워진다/

    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % (self.title, self.content, self.hit, str(self.regdate), self.user.id)