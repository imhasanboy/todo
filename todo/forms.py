from django import forms
from .models import ToDoListModel


class ToDoForms(forms.ModelForm):
    task_uz = forms.CharField()
    task_eng = forms.CharField()
    task_ru = forms.CharField()

    user_uz = forms.CharField()
    user_eng = forms.CharField()
    user_ru = forms.CharField()

    class Meta:
        model = ToDoListModel
        exclude = ['task', 'user']
