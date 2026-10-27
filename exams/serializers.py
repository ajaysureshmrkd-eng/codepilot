
from rest_framework import serializers

from exams.models import Assement
from problems.models import Question
from problems.serializers import Questionserializers
from django.db.models import Sum

from datetime import datetime

class AssementSerializer(serializers.ModelSerializer):

    question_count =serializers.SerializerMethodField(read_only=True)

    total_marks =serializers.SerializerMethodField(read_only=True)

    questions = serializers.SerializerMethodField(read_only=True)



    class Meta:

        model =Assement

        fields ="__all__"

        read_only_fields =["id","created_by","end_time"]


    def get_question_count(self,obj):

        return Question.objects.filter(assessment=obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assessment=obj).values("score").aggregate(total=Sum("score")).get("total")


    def get_questions(self,obj):

        questions_obj =Question.objects.filter(assessment=obj)

        serializers_inst =Questionserializers(questions_obj,many=True)

        return serializers_inst.data


    def validate(self, validated_data):

        exam_date =validated_data.get("exam_date")

        start_time =validated_data.get("start_time")

        exam_date_time =datetime.combine(exam_date,start_time)

        if datetime.now() >=  exam_date_time:

            raise serializers.ValidationError("invalid date")

        return validated_data

        





