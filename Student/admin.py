from django.contrib import admin
from .models import StudentInfo

# Register your models here.


class student_info_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'department', 'session')


admin.site.register(StudentInfo, student_info_Admin)

