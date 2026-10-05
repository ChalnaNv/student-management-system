from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def add_student(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            email=email,
            age=age,
            course=course
        )
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')

    return render(request, 'add_student.html')

def student_list(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {
        'students': students
    })
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']


        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')
        student.save()

    return render(request, 'edit_student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')

    return render(request, 'student_list.html', {
        'students': Student.objects.all()
    })

def home(request):
    total_students = Student.objects.count()

    return render(request, 'home.html', {
        'total_students': total_students
    })

