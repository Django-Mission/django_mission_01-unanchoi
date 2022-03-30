from django.shortcuts import render, redirect
import random
# Create your views here.


def index(request):
    numbers = [i for i in range(1, 46)]
    lotto_numbers = random.sample(numbers, 7)
    print(lotto_numbers)
    return render(request, "index.html", {"lotto_numbers": lotto_numbers})
