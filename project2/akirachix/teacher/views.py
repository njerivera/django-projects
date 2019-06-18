from django.shortcuts import render
# from django.shortcuts import render

from .forms import TeacherForm

def add_teacher(request):
	form = TeacherForm()
	return render(request,"add_teacher.html",{"form":form})

# Create your views here.
from django.shortcuts import render

# Create your views here.
