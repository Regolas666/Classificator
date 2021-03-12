from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_Class.urls'))  # При переходе на главную вызываем соотв. файл
]
