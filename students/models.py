from django.db import models

class Guardian(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Relationships = models.CharField(max_length=100)
    Guardian_Contact = models.CharField(max_length=11, null=True, blank=True)
    Student_Contact = models.CharField(max_length=11)


    def __str__(self):
        return f"{self.Last_name}, {self.First_name}"
    
class Instructor(models.Model):
    Instructor = models.CharField(max_length=100)
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Contact = models.CharField(max_length=11)
    Days = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.Instructor}"
    
class Grade(models.Model):
    Subject_Id = models.CharField(max_length=100)
    Student_num = models.IntegerField()
    Grade_Value = models.IntegerField()
    GPA = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.Grade_Value}"
    
class Student(models.Model):
    Student_Num = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Year_level = models.CharField(max_length=100)
    LRN = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.Student_Num}"
    
class Subject(models.Model):
    Subject_id = models.CharField(max_length=100)
    Subject_Name = models.CharField(max_length=100)
    Unit = models.IntegerField()
    Schedule = models.CharField(max_length=100)
    Room = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.Subject_id}"