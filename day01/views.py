import datetime

from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse



def hello():
    return "django"


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dc = {
    'username': 'test',
    'password': 'test123',
}

# Create your views here.
def view_func(request):

    url = reverse("v1")

    return redirect(url)

def view_func_v1(request):

    return HttpResponse(content="hello world v1")

def view_re_func(request):

    return HttpResponse(content="re world")

def view_template(request):

    return render(request, 'demo.html', context={
        'username': 'test',
        'foo': [n for n in range(10)],
        'func': hello(),
        'cls': Foo('test1', 18),
        'dc': dc
    })

def view_template_2(request):
    return render(request, 'filter.html', context={
        "name": "",
        "test": "TEST",
        "num1": 10,
        "num2": 20,
        "lis": [n for n in range(10)],
        "now": datetime.datetime.now,
    })