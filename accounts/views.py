from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer

from accounts.models import User


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