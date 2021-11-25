from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first(request):
    return render(request, 'main/first.html')


def second(request):
    header = "Team members"
    user1 = {"name": "Aiaru", "surname": "Sailau" }
    user2 = {"name": "Symbat", "surname": "Zhunisbayeva"}
    data = {"header": header, "user1": user1, "user2": user2}
    return render(request, 'main/second.html',context=data)


def third(request):
    header = "Developers"
    address = "Street Manasa 34A, Almaty"
    user1 = {"name": "Aiaru", "surname": "Sailau", "phone": "+7 707 151 28 04", "mail": "aiaruu.s@mail.ru"}
    user2 = {"name": "Symbat", "surname": "Zhunisbayeva", "phone": "+7 707 747 49 79", "mail": "zhunisbaeva00@gmail.com"}
    data = {"header": header, "adress": address, "user1": user1, "user2": user2}
    return render(request, 'main/third.html', context=data)


def home(request):
    return render(request, 'main/home.html')


def men(request):
    return render(request, 'main/men.html')


def women(request):
    return render(request, 'main/women.html')


def aboutus(request):
    return render(request, 'main/aboutus.html')

