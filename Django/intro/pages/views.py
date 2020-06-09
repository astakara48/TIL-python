from django.shortcuts import render

# Create your views here.
def index(request):
    hello = 'hello :)'
    lunch = '라멘'
    context = {
        'hello' : hello, 
        'l' : lunch
        }
    return render(request, 'pages/index.html', context)

def hello(request, name):
    context = {
        'name' : name
    }
    return render(request, 'pages/hello.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'pages/times.html', context)

from datetime import datetime
def dtl(request):
    foods = ['짜장면', '탕수육', '짬뽕', '양장피']
    sentence = 'Life is short, you need python'
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    
    context = {
        'foods' : foods,
        'sentence' : sentence,
        'fruits' : fruits,
        'datetimenow' : datetimenow,
        'emtpy_list' : empty_list,
    }
    return render(request, 'pages/dtl.html', context)

def birth(request, month, day):
    context = {
        'month' : month,
        'day' : day
    }
    return render(request, 'pages/birth.html', context)

def bday(request):
    # 1. 오늘 날짜 가져오기
    today = datetime.now()
    # 2. month, day 가져오기
    result = (today.month == 4 & today.day == 11)

    context = {
        'result' : result
    }
    return render(request, 'pages/bday.html', context)

def throw(request):
    context ={

    }
    return render(request, 'pages/throw.html', context)

def catch(request):
    message = request.GET.get('message') # => { message: 'hi'}
    username = request.GET.get('username')
    context = {
        'username' : username,
        'message' : message,
    }
    return render(request, 'pages/catch.html', context)

def lotto(request):
    context = {

    }
    return render(request, 'pages/lotto.html', context)

def generate(request):
    import random
    lotto = request.GET.get('lotto')
    lotto_num = []
    for i in range(int(lotto)):
        lotto_num.append(sorted(random.sample(range(1,46), 6)))
    context = {
        'lotto' : lotto,
        'lotto_num' : lotto_num,
    }
    return render(request, 'pages/generate.html', context)

def user_new(request):
    
    context = {

    }
    return render(request, 'pages/user_new.html', context)

def user_create(request):
    username = request.POST.get('username')
    pw = request.POST.get('pw')
    context = {
        'username' : username,
        'pw' : pw
    }
    return render(request, 'pages/user_create.html', context)