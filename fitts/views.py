from django.shortcuts import render, redirect
from .models import Tasks
from django.urls import reverse

# Create your views here.

def fitts(request):
    if request.method == "POST":
        for i in range(1, 9):
            transform = request.POST.get('transform', None)
            distance = request.POST.get('distance' + str(i), None)
            time = request.POST.get('time' + str(i), None)
            Tasks.objects.create(
                name = "김상현",
                age = 26,
                email = "abc@g.skku.edu",
                transform = transform,
                distance = distance,
                time = time
            )
        return redirect('fitts:fitts')
    elif request.method == "GET":
        return render(request, 'fitts/fittstask.html',{})