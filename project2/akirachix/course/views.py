
from django.shortcuts import render
from.models import Course
# from django.shortcuts import render

from .forms import CourseForm

def add_course(request):
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid(): 
		    form.save()
	
	else:
		form = CourseForm()
	return render(request,"add_course.html",{"form":form})

	form = CourseForm()
	return render(request,"add_course.html",{"form":form})

# Create your views here.
from django.shortcuts import render

def list_courses(request):
	courses = Course.objects.all()
	return render(request,"list_courses.html",{"courses":courses})
