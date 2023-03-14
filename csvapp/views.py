from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PersonalDetailsSerializer


class PersonalDetailsViews(APIView):
    def post(self,request):
        serializer=PersonalDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'success','data':serializer.data},status=status.HTTP_400_BAD_REQUEST)



    # Create your views here.
