from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse

# Create your views here.
def view_func(request):

    url = reverse("v1")

    return redirect(url)

def view_func_v1(request):

    return HttpResponse(content="hello world v1")

def view_re_func(request):

    return HttpResponse(content="re world")

def view_template(request):

    return render(request, 'demo.html')