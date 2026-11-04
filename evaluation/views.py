from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.generics import UpdateAPIView

from exams.models import Assement

from evaluation.models import Submission,Answer
from evaluation.permissions import IsStudentUser
from evaluation.serializers import SubmissionSerializer
from evaluation.serializers import AnswerSerializers

from problems.models import Question

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class SubmissionCreateView(APIView):


    # authentication_classes =[authentication.TokenAuthentication]

    authentication_classes =[JWTAuthentication]

    permission_classes =[permissions.IsAuthenticated,IsStudentUser]

    def post(self,request,pk=None):

        assessment_id =pk

        assessment_object =get_object_or_404(Assement,id=pk)

        inst =Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_int =SubmissionSerializer(inst)

        return Response (data=serializer_int.data)


class AnswercreateView(APIView):

    # authentication_classes =[authentication.TokenAuthentication]

    authentication_classes =[JWTAuthentication]

    permission_classes =[IsStudentUser]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        # validation start

        assessment_object = submission_object.assessment

        assessment_question = Question.objects.filter(assessment=assessment_object).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_question:

            raise serializers.ValidationError("invalid question,question no in asssessment")

        # validation end

        serializers_inst = AnswerSerializers(data=form_data)

        if serializers_inst.is_valid():

            serializers_inst.save(submission=submission_object)

            return Response (data=serializers_inst.data)

        else:

            return Response (data=serializers_inst.errors)



class SubmissionRetrieveView(APIView):


    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def get(self,request,pk=None):

        instance =get_object_or_404(Submission,id=pk)

        serializers_inst =SubmissionSerializer(instance)

        return Response (data=serializers_inst.data)



class AnswerUpdateView(UpdateAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]


    def patch(self,request,pk=None):


        answer_id =pk

        form_data = request.data

        answer_object = get_object_or_404(Answer,id=answer_id)

        serializers_inst =AnswerSerializers(data=form_data,instance=answer_object,partial=True)

        serializers_inst.fields["marks_awarded"].read_only =False

        serializers_inst.fields["feedback"].read_only=False

        if serializers_inst.is_valid():

            serializers_inst.save()

            # Answer.objects.filter(id=answer_id).update(**form_data)

            # response_data ={"meaage":"answer evaluated.."}

            # serializers_inst.save()

            return Response(data=serializers_inst.data)

        else:

            return Response(data=serializers_inst.errors)




