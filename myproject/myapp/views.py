from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def data(request):
    return render(request, 'myapp/data.html')

def test(request):
    return render(request, 'myapp/test.html')

def about(request):
    return render(request, 'myapp/about.html')







