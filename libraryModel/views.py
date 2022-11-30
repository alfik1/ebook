from ast import Delete
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Ebooks
from rest_framework import generics
from .serializer import EbookSerializer
from libraryModel import serializer
from django.db.models import Q
# Create your views here.


class GetEbooks(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ebooks.objects.all().order_by('-title')   
    serializer_class = EbookSerializer
    model = Ebooks
    


class CreateEbook(generics.ListAPIView):
   
    permission_classes = []
    
    def post(self,request):
        try:    
            data = request.data
            serializer = EbookSerializer(data=data)
            if serializer.is_valid():
                Ebooks.objects.create(**serializer.validated_data)
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors,status=406)
        except Exception as e:
            return Response(status=406)
   

class UpdateEbook(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request):
        data = request.data
        print(data)
        queryset = Ebooks.objects.get(id = data['id'])
        serializer = EbookSerializer(queryset,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(status=406)

class DeleteEbook(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id):
        try:
            Ebooks.objects.get(id = id).delete()
        except Exception:
            return Response(status=404)
        return Response({'deleted successfully'},status=200)

class SearchEbook(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            ebooks = Ebooks.objects.filter(Q(Title__icontains = data['details']) | Q(Author__icontains = data['details']) | Q(Genre__icontains = data['details']) |
            Q(Review__icontains = data['details']))
            
            serializer  = EbookSerializer(ebooks, many = True)
            return Response(serializer.data, status=200)
        except:
            return Response(status=400)
        