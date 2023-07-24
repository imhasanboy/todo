from django import forms
from .models import ToDoListModel


class ToDoForms(forms.ModelForm):
    task_uz = forms.CharField()
    task_eng = forms.CharField(required=False)
    task_ru = forms.CharField(required=False)

    user_uz = forms.CharField(required=False)
    user_eng = forms.CharField()
    user_ru = forms.CharField(required=False)

    class Meta:
        model = ToDoListModel
        exclude = ['task', 'user']
