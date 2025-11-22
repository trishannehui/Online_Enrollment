from django.urls import path
from . import views

urlpatterns = [
    path('guardian/', views.guardian_list, name='guardian_list'),
    path('guardian_create/', views.create_guardian, name='create_guardian'),
    path('guardian_edit/<int:student_id>', views.edit_guardian,name='edit_guardian'),
    path('guardian_delete/<int:student_id>', views.delete_guardian, name='delete_guardian'),
    path('instructor/', views.instructor_list, name='instructor_list'),
    path('instructor_create/', views.create_instructor, name='create_instructor'),
    path('instructor_edit/<int:student_id>', views.edit_instructor,name='edit_instructor'),
    path('instructor_delete/<int:student_id>', views.delete_instructor, name='delete_instructor'),
    path('grade/', views.grade_list, name='grade_list'),
    path('grade_create/', views.create_grade, name='create_grade'),
    path('grade_edit/<int:student_id>', views.edit_grade,name='edit_grade'),
    path('grade_delete/<int:student_id>', views.delete_grade, name='delete_grade'),
    path('', views.student_list, name='student_list'),
    path('student_create/', views.create_student, name='create_student'),
    path('student_edit/<int:student_id>', views.edit_student,name='edit_student'),
    path('student_delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('subject/', views.subject_list, name='subject_list'),
    path('subject_create/', views.create_subject, name='create_subject'),
    path('subject_edit/<int:student_id>', views.edit_subject,name='edit_subject'),
    path('subject_delete/<int:student_id>', views.delete_subject, name='delete_subject'),
]