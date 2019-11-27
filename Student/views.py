from django.shortcuts import render, redirect
from .models import StudentInfo
from .forms import StudentForm


def Student_Info_view(request):
    student_info = StudentInfo.objects.all()
    context = {'stdInfo': student_info}
    return render(request, 'student/information.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('student_information')
    else:
        form = StudentForm
    return render(request, 'student/add_student.html', {"form": form})


def edit_student(request, student_id):
    student = StudentInfo.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        form.save()
        return redirect('student_information')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit_student.html', {'form': form})


def delete_student(request, student_id):
    student = StudentInfo.objects.get(id=student_id)
    student.delete()
    return redirect('student_information')
