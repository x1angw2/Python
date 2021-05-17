from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    # return HttpResponse("First Pages")
    # return render(request, 'myfirst.html')
    return redirect('/home/')

def home(request):
    return HttpResponse('Home')
