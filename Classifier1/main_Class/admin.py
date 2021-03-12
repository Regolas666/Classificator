from django.contrib import admin
from .models import New


class NewAdmin(admin.ModelAdmin):
    list_display = [i.name for i in New._meta.fields]

    class Meta:
        model = New

admin.site.register(New, NewAdmin)
