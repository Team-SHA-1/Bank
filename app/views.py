from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .seriliazers import AccountSerializer
from .models import Account
from rest_framework.views import APIView
import json


class StudentAPI(APIView):
    def post(self,request,format=None):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None):
        pk = request.data["Account_Number"]
        account = Account.objects.get(Account_Number=pk)
        if account is None:
            return Response({'err':'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(account)
        return Response({'err':'No Error',"image_path" : serializer.data["Image"]})

class DataRetriveAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None):
        pk = request.data["Account_Number"]
        account = Account.objects.get(Account_Number=pk)
        if account is None:
            return Response({'err':'Account not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = AccountSerializer(account)
        res = {}
        for key in dict(request.data).keys():
            if "data" in key:
                res[key] = serializer.data[request.data[key]]
        return Response(res)
        



    
        
    
