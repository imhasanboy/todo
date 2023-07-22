from django.urls import path
from .views import (ListToDoApiView,DetailToDoApiView,CreateToDoApiView,
                    DeleteToDoApiView,UpdatePatchApiView,UpdatePutApiView,
                    StatusUpdateView)

urlpatterns = [
    path('', ListToDoApiView.as_view()),
    path('<pk>/', DetailToDoApiView.as_view()),
    path('create/', CreateToDoApiView.as_view()),
    path('delete/<int:pk>/', DeleteToDoApiView.as_view()),
    path('update_patch/<int:pk>/', UpdatePatchApiView.as_view()),
    path('update_put/<int:task_id>/', UpdatePutApiView.as_view()),
    path('status/<int:task_id>/', StatusUpdateView.as_view())
]