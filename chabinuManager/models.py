from tkinter import CASCADE
from django.db import models

# Create your models here.


# 매니저 계정 클래스
class managerAccount(models.Model) :
  
  managerNo = models.IntegerField                       #매니저 번호
  managerId = models.CharField(max_length=50)           #아이디
  managerPw = models.CharField(max_length=50)           #비밀번호
  lastLogin = models.DateTimeField()                    #마지막 로그인
  enrolldate = models.DateTimeField()                   #가입일


# 매니저 상세 정보 클래스
class manageDetail(models.Model) :
  
  managerNo = models.ForeignKey(to=managerAccount, on_delete=models.CASCADE)
  managerName = models.CharField(max_length=50)         
  managerAddress = models.CharField(max_length=100)
  managerPhone = models.CharField(max_length=20)












