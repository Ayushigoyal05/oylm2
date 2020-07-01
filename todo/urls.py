from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name="todo"),
    path('deletecomp/', views.delcomp, name="delcomp"),
    path('delall/', views.delall, name="delall"),
    path('complete/<todo_id>', views.complete, name="complete"),
    
]