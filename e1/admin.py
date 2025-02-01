from django.contrib import admin
from .models import Course, Student
# Register your models here.
# admin.site.register(Course)
# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
  list_display = ("name", "gender", "birth_day",)

class CourseAdmin(admin.ModelAdmin):
  list_display = ("name", "start_date", "end_date",)
  
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)