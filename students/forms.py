from django import forms
from .models import Guardian, Instructor, Grade, Student, Subject

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['First_name','Last_name', 'Relationships', 'Guardian_Contact', 'Student_Contact']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['Instructor','Fullname', 'Email', 'Contact', 'Days']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['Subject_Id','Student_num', 'Grade_Value', 'GPA', 'Remarks']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Student_Num','First_Name', 'Last_Name', 'Year_level', 'LRN']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['Subject_id','Subject_Name', 'Unit', 'Schedule', 'Room']

