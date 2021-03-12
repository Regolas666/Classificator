from django.shortcuts import render
import sqlite3

from .models import New
from .forms import NewForm, TextsFormSecond
from .Classificator import MainClassify as MC

# Вызываем здесь html-шаблоны.


def index(request):
    news = New.objects.all()  # наш список-набор элементов
    return render(request, 'main_Class/index.html', {'title': 'Главная страница сайта', 'news': news})


def classify(request):
    error = ''
    classText = ''
    if request.method == 'POST':
        form = TextsFormSecond(request.POST)
        secondForm = NewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text_news")
            classText = MC.choose_class(text)
        else:
            error = 'Попробуйте ввести другие данные'
    form = NewForm()
    secondForm = NewForm()
    context = {
        'form': form,
        'error': error,
        'predict': classText
    }
    return render(request, 'main_Class/classify.html', context)


"""
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()   # сохранение в базу данных
        else:
            error = 'Форма была неверной'
    form = NewForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main_Class/create.html', context)
"""


def handler404(request, exception):
    return render(request, 'main_Class/error404.html')


def handler500(request):
    return render(request, 'main_Class/error500.html')
