from django.contrib import admin
from core.models import Student

@admin.register(Student)
class College(admin.ModelAdmin):
    list_display = ['id', 'stuid', 'stuname', 'stuemail', 'stupass']
