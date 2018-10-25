from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        return render(request, 'random_word_app/index.html')
    else:
        return render(request, 'random_word_app/index.html')

def create(request):
    #if request.method == "POST":
    request.session['random']= get_random_string(length=14)
    request.session['count'] +=1
    return redirect('/')

def reset(request):
    if 'count' in request.session:
        request.session['count'] = 0
        request.session['random'] = ''
    return redirect('/')