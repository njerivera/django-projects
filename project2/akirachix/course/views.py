from django.shortcuts import render
# from django.shortcuts import render

from .forms import CourseForm

def add_course(request):
	form = CourseForm()
	return render(request,"add_course.html",{"form":form})

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
