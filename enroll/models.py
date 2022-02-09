from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
   # for custom user model
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=70, unique = True)
    subject = models.CharField(max_length = 70)
    def __str__(self):
        return self.stu_name


class Subject(models.Model):
    student_name = models.ManyToManyField(Student, related_name ='student1')
    subj_name = models.CharField(max_length=70)
    def student(self):
        return ",".join ([str(p) for p in self.student_name.all()])
    def __str__(self):
        return self.subj_name


class Teacher(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=70)


class Class(models.Model):
    stu = models.ForeignKey(Student,on_delete=models.CASCADE)
    class_name = models.CharField(max_length=70) 



#     This Signal create auth token for users
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)




                  # Custom User Model
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,):
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("user should have a email")
        user = self.model(username= username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, username, email, password= None):
        if password is None:
            raise TypeError('password should not be none')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique=True,db_index=True)
    # first_name = models.CharField(_("First name"), max_length=50)
    # first_name = models.CharField(max_length = 255, unique=True,db_index=True)
    # second_name = models.CharField(max_length = 255, unique=True,db_index=True)
    email = models.EmailField(max_length = 255, unique=True,db_index=True)
    is_verified = models.BooleanField(default= False)
    is_active= models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ""