from django.db import models

from exams.models import Assement

from accounts.models import User

# Create your models here.
class Question(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    score = models.PositiveIntegerField()

    assessment = models.ForeignKey(Assement,on_delete=models.CASCADE)

    sample_input = models.TextField(null=True)

    sample_output = models.TextField(null=True)

    question_number =models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at =models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title


    def save(self, *args,**kwargs):

        last_object =Question.objects.filter(movie=self.movie).last()

        if last_object:

            self.question_number =last_object =+1

        else:

            self.question_number =1


        return super().save( *args,**kwargs)

    