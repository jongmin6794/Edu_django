from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/<name>/',views.hello),
    path('hello/<name>/<apple>',views.hello),
    # 두 수를 입력 받아 곱한 결과를 보여주는 페이지
    path('times/<num1>/<num2>',views.times),
    # path('times/<str:num1>/<int:num2>',views.times),
    path('dtl/',views.dtl),
    # Is it your birthday? 오늘이 생일이면 '예', 아니면 '아니오'
    path('bday',views.bday),
    path('user_new/',views.user_new),
    path('user_create/', views.user_create),
]