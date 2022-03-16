from django.shortcuts import render

import chabinuManager

# Create your views here.

def login(request) :
  return render(request, 'chabinuManager/managerLogin.html')


def main(request) : 
  return render(request, 'chabinuManager/managerMain.html')