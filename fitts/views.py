from django.shortcuts import render, redirect
from .models import Tasks
from django.urls import reverse

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        age = request.POST.get('age')
        request.session['email']=email
        request.session['age']=age
        return redirect('fitts:fitts1')
    elif request.method == "GET":
        return render(request, 'fitts/login.html')

def fitts1(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age', None)
            email = request.session.get('email', None)
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts2')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask1.html',{})

def fitts2(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age')
            email = request.session.get('email')
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts3')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask2.html',{})

def fitts3(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age')
            email = request.session.get('email')
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts4')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask3.html',{})

def fitts4(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age')
            email = request.session.get('email')
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts5')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask4.html',{})

def fitts5(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age')
            email = request.session.get('email')
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts6')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask5.html',{})

def fitts6(request):
    if request.method == "POST":
        for i in range(1, 9):
            age = request.session.get('age')
            email = request.session.get('email')
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                age = age,
                email = email,
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:end')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask6.html',{})

def end(request):
    return render(request, 'fitts/end.html')