from ast import operator
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
# Create your views here.


def index(request):
    numbers = [i for i in range(1, 46)]
    lotto_numbers = random.sample(numbers, 7)
    print(lotto_numbers)
    return render(request, "index.html", {"lotto_numbers": lotto_numbers})


def practice(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operator = request.GET.get("operator")
    result = "{0} {1} {2}".format(num1, operator, num2)

    return render(request, "practice.html", {"result": result})

   # return HttpResponse("안녕하세요")
