from modeltranslation.translator import translator, TranslationOptions
from todo.models import ToDoListModel


class TodoTranslationOptions(TranslationOptions):
    fields = ('task',  'user')


translator.register(ToDoListModel, TodoTranslationOptions)
