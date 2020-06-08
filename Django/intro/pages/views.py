from django.shortcuts import render

# Create your views here.
def index(request):
    hello = 'hello :)'
    lunch = '라멘'
    context = {
        'hello' : hello, 
        'l' : lunch
        }
    return render(request, 'index.html', context)

def hello(request, name):
    context = {
        'name' : name
    }
    return render(request, 'hello.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'times.html', context)

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
    return render(request, 'dtl.html', context)

def birth(request, month, day):
    context = {
        'month' : month,
        'day' : day
    }
    return render(request, 'birth.html', context)

def bday(request):
    # 1. 오늘 날짜 가져오기
    today = datetime.now()
    # 2. month, day 가져오기
    result = (today.month == 4 & today.day == 11)

    context = {
        'result' : result
    }
    return render(request, 'bday.html', context)