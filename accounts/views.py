from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer,StudentProfileSerializer

from accounts.models import User,StudentProfile

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from evaluation.permissions import IsStudentUser

class AdminCreateView(APIView):


    def post(self,request):

        form_data =request.data

        serializer_inst =UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            instance =User.objects.create_superuser(role="admin",**cleaned_data)

            serializer_inst =UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class StudentCreateView(APIView):

    def post(self,request):

        form_data =request.data

        serializer_inst =UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst._validated_data

            instance =User.objects.create_user(**cleaned_data)


            serializer_inst=UserSerializer(instance)

            return Response(data= serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)


class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes =[permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):

        form_data = request.data

        student_profile_obj = StudentProfile.objects.get(student=request.user)

        serializer_inst = StudentProfileSerializer(data=form_data,instance=student_profile_obj)

        if serializer_inst.is_valid():

            serializer_inst.save()

            return Response (data= serializer_inst.data)

        else:

            return Response(data= serializer_inst.errors)

class profileDetailView(APIView):

    authentication_classes =[JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def get(self,request):

        instance =StudentProfile.objects.get(student=request.user)

        serializer =StudentProfileSerializer(instance)

        return Response (data=serializer.data)