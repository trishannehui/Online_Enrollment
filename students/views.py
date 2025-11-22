from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuardianForm, InstructorForm , GradeForm, StudentForm, SubjectForm
from .models import Guardian, Instructor, Grade, Student, Subject

#THIS IS THE Guardian
def create_guardian(request):
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guardian_list')
    else:
        form = GuardianForm()
    return render(request, 'create_guardian.html', {'form':form})

def edit_guardian(request, student_id):
    guardian = get_object_or_404(Guardian, id=student_id)
    form = GuardianForm(request.POST or None, instance=guardian)

    if form.is_valid():
        form.save()
        return redirect('guardian_list')
    
    return render(request, 'edit_guardian.html', {'form':form})

def guardian_list(request):
    guardians = Guardian.objects.all()
    return render(request, 'guardian_list.html', {'guardians':guardians})

def delete_guardian(request, student_id):
    guardian = get_object_or_404(Guardian, id=student_id)
    guardian.delete()
    return redirect ('guardian_list')


#THIS IS THE Instructor
def create_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm()
    return render(request, 'create_instructor.html', {'form':form})

def edit_instructor(request, student_id):
    instructor = get_object_or_404(Instructor, id=student_id)
    form = InstructorForm(request.POST or None, instance=instructor)

    if form.is_valid():
        form.save()
        return redirect('instructor_list')
    
    return render(request, 'edit_instructor.html', {'form':form})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors':instructors})

def delete_instructor(request, student_id):
    instructor = get_object_or_404(Instructor, id=student_id)
    instructor.delete()
    return redirect ('instructor_list')


#THIS IS THE GRADE
def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'create_grade.html', {'form':form})

def edit_grade(request, student_id):
    grade = get_object_or_404(Grade, id=student_id)
    form = GradeForm(request.POST or None, instance=grade)

    if form.is_valid():
        form.save()
        return redirect('grade_list')
    
    return render(request, 'edit_grade.html', {'form':form})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades':grades})

def delete_grade(request, student_id):
    grade = get_object_or_404(Grade, id=student_id)
    grade.delete()
    return redirect ('grade_list')


#THIS IS THE STUDENT
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form':form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')
    
    return render(request, 'edit_student.html', {'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect ('student_list')


#THIS IS THE SUBJECT
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'create_subject.html', {'form':form})

def edit_subject(request, student_id):
    subject = get_object_or_404(Subject, id=student_id)
    form = SubjectForm(request.POST or None, instance=subject)

    if form.is_valid():
        form.save()
        return redirect('subject_list')
    
    return render(request, 'edit_subject.html', {'form':form})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects':subjects})

def delete_subject(request, student_id):
    subject = get_object_or_404(Subject, id=student_id)
    subject.delete()
    return redirect ('subject_list')