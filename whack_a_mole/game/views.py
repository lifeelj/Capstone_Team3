from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Result

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'game/home.html')
    elif request.method == "POST":
        age = request.POST.get('age')
        pk = 0
        if age == "ten":
            pk = 0
        elif age == "thirty":
            pk = 1
        elif age == "fifty":
            pk = 2
        request.session['age'] = pk
        return redirect('game:game', pk=pk)


def game(request, pk):
    if request.method == "GET":
        data = {
            'pk': pk,
            'mu': 9.2,
        }
        return render(request, 'game/game.html', data)
    elif request.method == "POST":
        age = request.session.get('age')
        score = request.POST.get('score')
        Result.objects.create(
            age=age,
            score=score
        )
        return redirect('game:game', pk=pk)
