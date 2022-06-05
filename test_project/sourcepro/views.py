from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import models
from .models import *
import ast
from rest_framework.renderers import JSONRenderer
from django.core import serializers as core_serializers
from rest_framework.decorators import api_view
from .serializers import *



@api_view(['GET'])
def home(request):
    info1 = all_courses.objects.filter(type = "new")
    serializer1 = all_courses_serializer(info1, many=True)

    info3 = all_courses.objects.filter(type="All")
    info3_serializer = all_courses_serializer(info3, many=True)


    for i in range(0, len(serializer1.data)):
        serializer1.data[i]["chapters_vls"] = ast.literal_eval(serializer1.data[i]["chapters_vls"])

    for i in range(0, len(info3_serializer.data)):
        info3_serializer.data[i]["chapters_vls"] = ast.literal_eval(info3_serializer.data[i]["chapters_vls"])

    info2 = usr_course.objects.filter(status = "in progress")
    serializer2 = usr_course_serializer(info2, many=True)
    print(serializer2.data[0])


    for i in serializer2.data:
        i.pop("deactivation_days_left")
        i.pop("course_release_date")
        i.pop("minutes_Completed")

    for i in serializer1.data:
        i.pop("chapters_vls")
        i.pop("course_description")
        i.pop("FAQs")
        i.pop("type")

    for i in info3_serializer.data:
        i.pop("chapters_vls")
        i.pop("course_description")
        i.pop("FAQs")
        i.pop("type")

    '''
    lst1 = [] #this list is for the for loop
    lst2 = []
    lst3 = []
    for i in range(0, len(info2)):
        id = serializer2.data[i]["Course_id"]
        a = all_courses.objects.filter(id = id)
        aa = all_courses_serializer(a, many=True)
        lst1.append([{"Course_id":serializer2.data[i]["Course_id"]},
                    {"percentage_completed":serializer2.data[i]["percentage_completed"]},
                    {"minutes_Completed":serializer2.data[i]["minutes_Completed"]},
                    {"minutes_left":serializer2.data[i]["minutes_left"]},
                    {"thumbnail": aa.data[i]["thumbnail"]},
                    {"name":aa.data[i]["name"]}])

    for j in range(0, len(info1)):
        lst2.append([{"Course_id":serializer1.data[j]["id"],
                      "Name": serializer1.data[j]["name"],
                      "total duration":serializer1.data[j]["total_duration"]}])

    for k in range(0, len(info3)):
        lst3.append([{"Course_id":info3_serializer.data[j]["id"],
                      "Name": info3_serializer.data[j]["name"],
                      "total duration":info3_serializer.data[j]["total_duration"]}])
    '''
    return JsonResponse({"user courses": serializer2.data,
                         "New courses": serializer1.data,
                         "all courses": info3_serializer.data})
    #return JsonResponse({"continue learning": lst1,"New courses": lst2,"All courses": lst3})

@api_view(['GET'])

def mycourses(request):
    d = usr_course.objects.all()
    dd = usr_course_serializer(d,many=True)

    for i in dd.data:
        i.pop("minutes_Completed")

    for n in range(0,len(dd.data)):
        x = dd.data[n]["Course_id"]
        e = all_courses.objects.filter(Course_id = x)
        ee= all_courses_serializer(e,many= True)
        dd.data[n]["thumbnail"] = ee.data[n]["thumbnail"]

    # d = usr_course.objects.get(status="in progress")
    # dd = usr_course_serializer(d, many=False)
    #
    # f = usr_course.objects.get(status = "completed")
    # ff = usr_course_serializer(f, many=False)
    #
    # return JsonResponse({"In progress": dd.data, "History": ff.data})
    return JsonResponse({"user courses":dd.data})


@api_view(['GET'])
def in_course(request,pk):
    a = all_courses.objects.filter(id = pk)
    aa = all_courses_serializer(a, many = True)

    aa.data[0]["chapters_vls"] = ast.literal_eval(aa.data[0]["chapters_vls"])

    return JsonResponse({"chapter_vls":aa.data[0]["chapters_vls"],
                         "Course_description":aa.data[0]["course_description"],
                         "FAQS":aa.data[0]["FAQs"]}, safe= False)
    # for i in range(0,len(a1)):
    #     l.append({"chapter_vls":aa.data[0]["chapters_vls"],"course_description":aa.data[0]["course_description"],
    #               "FAQs": aa.data[0]["FAQs"]})
    # return JsonResponse(l, safe=False)

@api_view(['GET'])
def quiz(request,pk):
    b = quizes.objects.filter(course_id = pk)
    bb = quiz_serializer(b, many = True)
    bb.data[0]["que_options"] = ast.literal_eval(bb.data[0]["que_options"])
    return JsonResponse(bb.data, safe = False)