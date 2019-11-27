from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('', views.Student_Info_view, name='student_information'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>', views.delete_student, name='delete_student'),
]
