from django.shortcuts import render

# Create your views here.


def FirstPage(request):

    return render(request,"main4.html")


def SecondPage(request):

    return render(request,"heart.html")