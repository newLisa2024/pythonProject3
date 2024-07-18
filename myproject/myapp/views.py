from django.http import HttpResponse

def index_view(request):
    return HttpResponse("<h1>Это мой первый проект на Django.</h1>")

def data_view(request):
    return HttpResponse("<h1>Вторая страница проекта на Django - data.</h1>")

def test_view(request):
    return HttpResponse("<h1>Третья страница проекта на Django - test.</h1>")


