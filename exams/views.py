from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView

from exams.models import Assement
from exams.serializers import AssementSerializer
from datetime import timedelta,datetime
from exams.permission import Isowner


# class AssementListView(APIView):

#     authentication_classes =[authentication.TokenAuthentication]

#     permission_classes =[permissions.IsAuthenticated]

#     def get(self,request):

#         qs =Assement.objects.all()

#         serializers_inst =AssementSerializer(qs,many=True)

#         return Response(data=serializers_inst.data)

#     # def post(self,request):

#     #     form_data =request.data

#     #     serializer_inst =AssementSerializer(data= form_data)

#     #     if serializer_inst.is_valid():

#     #         serializer_inst.save(created_by =request.user)

#     #         # cleaned_data =serializer_inst.validated_data

#     #         # examdate =cleaned_data.get("exam_date")

#     #         # starttime =cleaned_data.get("start_time")

#     #         # duration =cleaned_data.get("duration")

#     #         # examdatetime =datetime.combine(examdate,starttime) + timedelta(hours=duration)

#     #         # cleaned_data["end_time"] =examdatetime.time()

#     #         # instance =Assement.objects.create(created_by =request.user,**cleaned_data)

#     #         # serializer_inst =AssementSerializer(instance)

#     #         return Response(data=serializer_inst.data)

#     #     else:

#     #         return Response (data=serializer_inst.errors)


# class AssementRetrieveUpdateDeleteView(APIView):

#     authentication_classes =[authentication.TokenAuthentication]

#     permission_classes =[Isowner]

#     def get(self,request,pk=None):

#      instance =get_object_or_404(Assement,id=pk)

#      self.check_object_permissions(request,instance)

#      serializer_inst =AssementSerializer(instance)

#      return Response (data= serializer_inst.data)


#     def put(self,request,pk=None):

#         instance =get_object_or_404(Assement,id=pk)

#         self.check_object_permissions(request,instance)

#         form_data =request.data

#         serializers_inst =AssementSerializer(data=form_data,instance=instance)

#         if serializers_inst.is_valid():

#             serializers_inst.save(created_by =request.user)

#             # cleaned_data =serializers_inst.validated_data

#             # examdate =cleaned_data.get("exam_date")

#             # starttime =cleaned_data.get("start_time")

#             # duration =cleaned_data.get("duration")

#             # exam_date_time =datetime.combine(examdate,starttime) +timedelta(hours=duration)

#             # instance =serializers_inst.save(end_time=exam_date_time.time())

#             # serializers_inst =AssementSerializer(instance)

#             return Response (data=serializers_inst.data)

#         else:

#             return Response (data= serializers_inst.errors)

#     def delete(self,request,pk=None):

#         instance =get_object_or_404(Assement,id=pk)

#         self.check_object_permissions(request,instance)

#         instance.delete()

#         return Response ({"message":"deleted...."})



class AssementListView(ListAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]

    serializer_class =AssementSerializer

    queryset =Assement.objects.all()



class AssementCreateView(CreateAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def post(self,request):

        form_data =request.data

        serializer_inst =AssementSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            serializer_inst.save(created_by=request.user)

            return Response (data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)

class AssementRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[Isowner]

    serializer_class =AssementSerializer

    queryset =Assement.objects.all()

    


        

        

        

        




    