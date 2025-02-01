from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from e1.models import Course
from .forms import CourseNewForm 
from django.shortcuts import redirect
# Create your views here.

def home (request):
    return render(request, 'app_home/index.html')

def courses(request):
    courses = Course.objects.all()  # Lấy tất cả các khóa học
    template = loader.get_template('app_home/courses.html')  # Template hiển thị
    context = {
        'courses': courses,  # Đổi 'course' thành 'courses' để khớp với template
    }
    return HttpResponse(template.render(context, request))


def edit_course(request):
    course = Course.objects.get(id = 1)
    template = loader.get_template('app_home/course-edit.html')
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))

def CourseNew(request):
    if request.method == "POST":
        print("POST data:", request.POST)  # In dữ liệu POST để kiểm tra
        form = CourseNewForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Xác nhận form hợp lệ
            return HttpResponseRedirect("/courses")
        else:
            print("Form errors:", form.errors)  # Hiển thị lỗi nếu có
    else:
        form = CourseNewForm()

    template = loader.get_template('app_home/course-new.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
