
from rest_framework import serializers

from exams.models import Assement

from datetime import datetime

class AssementSerializer(serializers.ModelSerializer):


    class Meta:

        model =Assement

        fields ="__all__"

        read_only_fields =["id","created_by","end_time"]


    def validate(self, validated_data):

        exam_date =validated_data.get("exam_date")

        start_time =validated_data.get("start_time")

        exam_date_time =datetime.combine(exam_date,start_time)

        if datetime.now() >=  exam_date_time:

            raise serializers.ValidationError("invalid date")

        return validated_data

        





