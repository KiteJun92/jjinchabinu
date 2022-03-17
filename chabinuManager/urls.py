from django.urls import path
from . import views

# 다른 앱과의 충돌 방지를 위해 app_name 추가
app_name = 'chabinuManager'

# 주소 매핑
urlpatterns = [

  path('', views.login, name='login'),
  path('main/', views.main, name='main'),
  path('workList/', views.workList, name='workList'),


]