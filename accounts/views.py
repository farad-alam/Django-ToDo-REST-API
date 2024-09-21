from django.shortcuts import render, HttpResponse

# Create your views here.


def registration_view(request):
    return HttpResponse('sound from accounts!!!')