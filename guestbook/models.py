from django.db import models

# Create your models here.

class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    message = models.CharField(max_length=2000)#(본문내용)
    regdate = models.DateTimeField(auto_now= True) # 들어갈때 자동으로 현시간을 가져옴



    def __str__(self): # toString
        return 'Guestbook(%s, %s, %s, %s)' % (self.name, self.password, self.message, str(self.regdate))

