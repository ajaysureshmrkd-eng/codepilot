from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from exams.models import Assement
from problems.serializers import Questionserializers
from problems.models import Question

# Create your views here.

class QuestionCreateView(CreateAPIView):


    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def post(self,request,pk=None):


        assessment_id =pk

        assessment_object =Assement.objects.get(id =assessment_id)

        form_data =request.data

        serializer_inst =Questionserializers(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(assessment =assessment_object,created_by =request.user)

            return Response(data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)


class RetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    serializer_class =Questionserializers

    queryset =Question.objects.all()



            