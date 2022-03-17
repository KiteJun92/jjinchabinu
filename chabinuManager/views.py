from django.shortcuts import render

import chabinuManager

# Create your views here.

# 로그인 페이지 (login)
def login(request) :
  return render(request, 'chabinuManager/managerLogin.html')

# 매니저 시작 메인 페이지 (main)
def main(request) : 
  return render(request, 'chabinuManager/managerMain.html')

# 매니저 작업 목록 페이지 (workList)
def workList(request) : 
  return render(request, 'chabinuManager/managerworkList.html')