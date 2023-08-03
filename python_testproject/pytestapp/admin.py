from django.contrib import admin
from pytestapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stname','srollno','sbranch','sbloodgroup']

admin.site.register(Student,StudentAdmin)
