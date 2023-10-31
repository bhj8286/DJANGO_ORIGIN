from django.shortcuts import render
import random
from faker import Faker

# Create your views here.

def index(request):
    return render(request, 'index.html')


def hello(request):
    username = '배호진'

    result = {
        'username': username,
    }

    return render(request, 'hello.html', result)

def dinner(request):
    menus = ['김밥','돈가스','스파게티']
    pick = random.choice(menus)

    result = {
        'pick': pick,
    }

    return render(request, 'dinner.html', result)

def lotto(request):
    numbers = random.sample(range(1,46),6)

    result = {
        'numbers': numbers,
    }

    return render(request, 'lotto.html', result)


def greeting(request, name):
    
    result = {
        'name': name,
    }

    return render(request, 'greeting.html', result)

def cube(request, num):
    result = {
        'num':num,
        'cube':num**3,
    }

    return render(request, 'cube.html', result)

def posts(request):
    posts = []

    fake = Faker()

    for i in range(100):
        posts.append(fake.text())

    result = {
        'posts':posts,
    }

    return render(request, 'posts.html', result)