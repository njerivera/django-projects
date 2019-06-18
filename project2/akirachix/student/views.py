from django.shortcuts import render
from django.shortcuts import render

from .forms import StudentForm

def add_student(request):
	form = StudentForm()
	return render(request,"add_student.html",{"form":form})

# Create your views here.
