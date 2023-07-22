from django.contrib import admin
from .models import ToDoListModel
from .forms import ToDoForms


class ToDoAdmin(admin.ModelAdmin):
    form = ToDoForms
    list_display = ('task', 'user')
    search_fields = ('task',)


# Register your models here.
admin.site.register(ToDoListModel, ToDoAdmin)
