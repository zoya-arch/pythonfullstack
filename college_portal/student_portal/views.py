from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data1={
        'name':"abc",
        'age':19,
        'department':"BCA"
    }
    marks=[100,98,97]
    return render(request,'home.html',{
        'data1':data1,
        'marks1':marks
    })
def about(request):
    return HttpResponse("Welcome to about page")
def contact(request):
    return HttpResponse("Welcome to contact page")