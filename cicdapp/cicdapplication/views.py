from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("hey hello I'm there")