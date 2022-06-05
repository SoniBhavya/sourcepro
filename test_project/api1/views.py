from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import models
from .models import *
import ast
import json
from rest_framework.renderers import JSONRenderer

from django.core import serializers as core_serializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

l1 = [{"id": "11", "name": "IT", "total duration": "60", "thumb_nail": "img_link"},
        {"id": "22", "name": "Public administration", "total duration": "120", "thumb_nail": "img_link"},
        {"id": "33", "name": "History", "total duration": "300", "thumb_nail": "img_link"},
        {"id": "44", "name": "Artificial Intelligence", "total duration": "67", "thumb_nail": "img_link"}]

l2 = [{"id": "55", "name": "Python", "total duration": "60", "thumb_nail": "img_link", "duration_completed": "30", "status": "inprogress"},
         {"id": "66", "name": "R Programming", "total duration": "120", "thumb_nail": "img_link", "duration_completed": "30", "status": "completed"},
         {"id": "77", "name": "C++", "total duration": "300", "thumb_nail": "img_link", "duration_completed": "30", "status": "inprogress"},
         {"id": "88", "name": "C", "total duration": "68", "thumb_nail": "img_link", "duration_completed": "30", "status": "completed"}]


@api_view(['GET'])
def gdata(request):
    #info1 = all_course.objects.all().order_by('-id')
    info1 = all_course.objects.all()
    fields = ("thumbnail","name","id")
    print("info1",info1)
    serializer1 = all_course_serializer(info1, many=True)

    print("All course",type(serializer1.data[0]["chapters_vls"]))

    serializer1.data[0]["chapters_vls"] = ""

    for i in range(0, len(serializer1.data)):
        serializer1.data[i]["chapters_vls"] = ast.literal_eval(serializer1.data[i]["chapters_vls"])

    #print("All course list", type(serializer1.data[0]["chapters_vls"]))
    info2 = user_courses.objects.all()
    #print("Type info1", info2)
    serializer2 = user_course_serializer(info2, many=True)
    #print("serializer", serializer2.data)

    #print("asasasas",user_courses.objects.filter(Course_id__in=[1, 4, 7]))
    #info2 = core_serializers.serialize("json", user_courses.objects.filter(pk__in= [1,4,7]))
    #print("**************info2:",info2)
    #print(type(info2))
    return JsonResponse({"continue learning": serializer2.data, "New courses": serializer1.data})
    # dict = {"New Courses": l1, "Continue Learning": l2}
    # return Response(dict)

@api_view(['GET'])
def mycoursesinprog(request):
    d = user_courses.objects.get(status = "in progress")
    dd = user_course_serializer(d, many=False)
    return JsonResponse(dd.data)


@api_view(['GET'])
def mycoursescompleted(request):
    f = user_courses.objects.get(status = "completed")
    ff = user_course_serializer(f, many=False)
    return JsonResponse(ff.data)


@api_view(['POST'])
def pdata(request):
    print("*******************************REQUEST:", request)
    # if request == 'POST':
    password = request.data["password"]
    u_name = request.data["u_name"]
    print("type of entered data", type(password))
    l = [password, u_name]
    return Response(l)
    # else:
    #     return render(request, "login.html")

@api_view(['GET','POST'])
def signin(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        password = request.data["password"]
        u_name = request.data["u_name"]
        user = authenticate(request, username=u_name, password=password)
        if user is not None:
            print("user is not none")
            login(request, user)
            return redirect(home,u_name)
        else:
            return render(request, "login.html")

def signout(request):
    logout(request)
    return redirect(signin)

@api_view(['GET'])
@login_required(login_url='login')
def home(request,pk):
    #result = request.user
    session = request.session.session_key
    request.session.set_expiry(10)
    details = models.login_details.objects.get(email=pk)
    serializer = HeroSerializer(details, many=False)
    return Response(serializer.data)

    # if request == "GET":
    #     print("*************in request == GET")
    #     #return render(request, "home.html")
    #     details = login_details.objects.get(email=pk)
    #     print("-----------------details", details)
    #     serializer = HeroSerializer(details, many=False)
    #     return Response(serializer.data)
    # return render(request, "home.html",{"result":result,"sessions":session})




user_list = ['a','b']
password = ['aa','bb']
# Create your views here.
@csrf_exempt
def signin(request):
    if request.method == "POST":
        password = request.POST["password"]
        u_name = request.POST["u_name"]
        #if mailone in user_list and u_name in password:
        user = authenticate(request,username=u_name, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request,"login.html")
    else:
        return render(request, "login.html")


# # this is original login method
# if request.method == 'POST' and "email" in request.POST and "password" in request.POST:
#     email = request.POST['email']
#     password = request.POST['password']
#     data = {"email": email,"password":password}
#     print(data)
#
#     if models.login_details.objects.filter(email=email,password = password).exists():
#         return HttpResponse("Details validated.")
#     else:
#         if models.login_details.objects.filter(email = email).exists():
#             return HttpResponse("incorrect password")
#         else:
#             return HttpResponse("record not found")
# else:
#     return HttpResponse("No details entered")
