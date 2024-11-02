from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Student
from django.views import View
from .forms import AddStudentForm
# Create your views here.

def home(request):
    stu_data=Student.objects.all()
    return render(request,'core/home.html',{'stu_data':stu_data})

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')         
    else:
        form = AddStudentForm()

    return render(request, 'core/add.html', {'form': form})

def delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')

def edit_view(request, id):
    student = get_object_or_404(Student, id=id) 

    if request.method == 'POST':
        form = AddStudentForm(request.POST, instance=student)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = AddStudentForm(instance=student)  

    return render(request, 'core/edit.html', {'form': form, 'student': student})