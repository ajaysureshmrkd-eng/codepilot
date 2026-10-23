from django.db import models

# Create your models here.


from accounts.models import User


class Assement(models.Model):

    title =models.CharField(max_length=200)

    batch =models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
    ('python', 'python'),
    ('java', 'java'),
    ('c', 'c'),
    ("cpp","c++"),
    ("javascript","javascript")
)

    STATUS_CHOICES = (
    ('draft', 'draft'),
    ('published', 'published'),
    ('completed', 'Completed'),
)

    language =models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    status =models.CharField(max_length=200,choices=STATUS_CHOICES,default="draft")

    exam_date =models.DateField()

    duration =models.PositiveBigIntegerField()

    start_time =models.TimeField()

    end_time =models.TimeField(null=True)

    created_by =models.ForeignKey(User,on_delete=models.CASCADE)

    