from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    data={
        'name':"abc",
        'age':19,
        'department':"BCA"
    }
    marks=[100,98,97]
    return render(request,'home.html',{'data1':data,'marks1':marks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def forms1(request):
    if request.method=='POST':
        reg_no=request.POST.get('reg_no')
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        return render(request,'Student_form.html',{'message':"saved successfully"})
    return render(request,'Student_form.html')
def Student_form_dj(request):
    if request.method=="POST":
        form=Student_form_data(request.POST)
        if form.is_valid():
            reg_no1=form.cleaned_data['reg_no1']
            name1=form.cleaned_data['name1']
            email1=form.cleaned_data['email1']
            return HttpResponse("Saved successfully")
        else:
            return HttpResponse("Inavlid data")
    else:
        form=Student_form_data()
        return render(request,'student_form_data.html',{'form':form})
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')
def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponse("You have logged out successfully")
    return HttpResponse("Invalid request")


    