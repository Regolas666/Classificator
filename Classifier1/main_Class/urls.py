from django.urls import path
from . import views

# здесь вызывем Views (что у нас должно открываться, опред. html-шаблон)
urlpatterns = [
    path('', views.index, name='home'),
    path('classify', views.classify, name='classify'),
#   path('create', views.create, name='create'),
#  path('getAll', views.getAll, name='getAll'),
]
