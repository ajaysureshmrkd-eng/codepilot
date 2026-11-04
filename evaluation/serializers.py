
from rest_framework import serializers

from evaluation.models import Submission,Answer



class SubmissionSerializer(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField(read_only=True)

    student = serializers.StringRelatedField(read_only=True)

    answers = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Submission

        fields ="__all__"

        read_only_fields = [fields] 


    def get_answers(self,obj):

        answer_obj = Answer.objects.filter(submission=obj)

        serializers_int =AnswerSerializers(answer_obj,many=True)

        return serializers_int.data


        # def get_fields(self):

        #     fields =super().get_fields()

        #     for field in fields.values():

        #         field.read_only =True

        #     return fields

from problems.models import Question
class AnswerSerializers(serializers.ModelSerializer):

    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:

        model = Answer

        fields = "__all__"

        read_only_fields = ["id","submission","marks_awarded","feedback","evaluated_at"]



    # def validate(self, validated_data):

        # marks_awarded =

        