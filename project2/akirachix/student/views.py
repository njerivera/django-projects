from django.shortcuts import render
from.models import Student
# from django.shortcuts import render

from .forms import StudentForm

def add_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid(): 
		    form.save()
	
	else:
		form = StudentForm()
	return render(request,"add_student.html",{"form":form})

	form = StudentForm()
	return render(request,"add_student.html",{"form":form})

# Create your views here.
from django.shortcuts import render

def list_students(request):
	students = Student.objects.all()
	return render(request,"list_student.html",{"students":students})
