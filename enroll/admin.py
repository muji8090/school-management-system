from django.contrib import admin
from .models import Student, Teacher, Subject ,Class, User

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','stu_name','subject']

@admin.register(Subject)
class   SubjectAdmin(admin.ModelAdmin):
    list_display=['id','subj_name','student']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','subject','tech_name']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=['id','stu','class_name']

@admin.register(User)
class ClassAdmin(admin.ModelAdmin):
    list_display=['id','email','password', 'username']