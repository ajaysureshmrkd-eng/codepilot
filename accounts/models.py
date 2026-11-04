from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    phone =models.CharField(max_length=12,unique=True)

    ROLE_CHOICES=(
        ("student","student"),
        ("admin","admin")
    )

    role =models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")   

from django.db.models.signals import post_save


class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linked_url = models.URLField(null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")


def  create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role =="student":

        StudentProfile.objects.create(student=instance)


post_save.connect(create_student_profile,sender=User)


from django.core.mail import send_mail


def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role =="student":

        send_mail(
        "account creation comformation",
        "you have successfully created user in codepilot application",
        "ajaysureshmrkd@gmail.com",
        ["ajayes7306@gamil.com"],
    )

post_save.connect(send_invitation_mail,sender=User)