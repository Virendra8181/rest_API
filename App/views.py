from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse
from .models import Tata
from .serializer import Tataserializer ,userserializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response

@csrf_exempt 
def Tatalist(request):
    if request.method=="GET":
       tata= Tata.objects.all()
       
       ser=Tataserializer(tata, many = True)
       return JsonResponse(ser.data ,safe = False)

    elif request.method=="POST":
        jsondata=JSONParser().parse(request)
        seri = Tataserializer(data=jsondata)
        if seri.is_valid():
            seri.save() 
            return JsonResponse(seri.data,safe=False)  
        else:
            return JsonResponse(seri.errors,safe=False)
@csrf_exempt 
def Empmethod(request,pk):

    try:
        Emp=Tata.objects.get(pk=pk)
    except Tata.DoesNotExist:
        return HttpResponse (status= 404)

    if request.method =='DELETE':
        Emp.delete()
        return HttpResponse("delete is succsefull")

    elif request.method == 'PUT':
        jsondata=JSONParser().parse(request)
        serialzer=Tataserializer(Emp,data=jsondata)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data,safe=False)
        
    elif request.method == 'GET':
        ser=Tataserializer(Emp)
        return JsonResponse(ser.data, safe= False)

@api_view(['GET','POST'])
def viewlist(request,pk):
    try:
        Emp=Tata.objects.get(pk=pk)
    except Tata.DoesNotExist:
        return HttpResponse (status= 404)
    
    if request.method== 'POST':
        serialzer=Tataserializer(Emp,data=request.data)
        if serialzer.is_valid:
            serialzer.save()
            return Response(serialzer.data)

    elif request.method =='GET':
        serialzer=Tataserializer(Emp)
        return Response(serialzer.data)


@csrf_exempt
def Userlist(request):
    if request.method=="GET":
        users=User.objects.all()
        serlializer=userserializer(users, many=True)
        return JsonResponse (serlializer.data ,safe=False)

    

    