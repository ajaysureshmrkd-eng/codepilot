from django.db import models

# Create your models here.


from accounts.models import User

from datetime import datetime,time,timedelta


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

    def __str__(self):
        return f"{self.title} : {self.exam_date}"



    def save(self,*args,**kwargs):

        end_date_time =datetime.combine(self.exam_date,self.start_time) +timedelta(hours=self.duration)

        self.end_time =end_date_time.time()

        return super().save(*args,**kwargs)

    