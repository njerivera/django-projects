from django.shortcuts import render
from.models import Teacher
# from django.shortcuts import render

from .forms import TeacherForm

def add_teacher(request):
	if request.method == "POST":
		form = TeacherForm(request.POST)
		if form.is_valid(): 
		    form.save()
	
	else:
		form = TeacherForm()
	return render(request,"add_teacher.html",{"form":form})

	form = TeacherForm()
	return render(request,"add_teacher.html",{"form":form})

# Create your views here.
from django.shortcuts import render

def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request,"list_teachers.html",{"teachers":teachers})
