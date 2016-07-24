from django.shortcuts import render,render_to_response
from myApp import models

def Details(request):
    c = {}
    students = models.studentRecord.objects.all()
    c['students'] = students
    return render_to_response('details.html',c)

