# -*- coding: gbk -*-

from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
import json
from PIL import Image
sys.path.append(r'/home/lyx/object_detection/Deformable_FPN_DOTA/experiments/fpn/')
sys.path.append(r'/home/lyx/Deformable_FPN_DOTA/fpn/')


import od_lyx


# Create your views here.

def index(request):
    HttpResponse(u"hello!")
    return render(request, 'uploadFile.html')

def upload_file(request):  
    #assert False, request.POST
       
    if request.method == "POST":   
        myFile =request.FILES.get("myfile", None)      
        if not myFile:  
            return HttpResponse(u"no files for upload!")  

        destination = open(os.path.join("/home/lyx/django",myFile.name),'wb+')     
        for chunk in myFile.chunks():      
            destination.write(chunk)  
        destination.close()  
        
        data = mnist_app.main(os.path.join("/home/lyx/django",myFile.name))#int
      
        return HttpResponse(data)  



file_name_list = []


def fileupload(request):
    del file_name_list[:]
    files = request.FILES.getlist('files[]')
    #file_name_list = []
    for f in files:
        #destination = 'd:/temp/'  # windows
        destination = '/home/lyx/django/test_upload/static/images/'  # linux
        if not os.path.exists(destination):
            os.makedirs(destination)
        with open(destination+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        file_name_list.append(f.name)

    return HttpResponse(file_name_list)


def object_detection(request):
    if request.method == "GET":
        print request.GET
        print type(request.GET)
        print request.GET.get('x1')
        print request.GET.get('y1')
        print request.GET.get('x2')
        print request.GET.get('y2')
        x1=float(request.GET.get('x1'))
        y1=float(request.GET.get('y1'))
        x2=float(request.GET.get('x2'))
        y2=float(request.GET.get('y2'))

        img = Image.open(os.path.join("/home/lyx/django/test_upload/static/images",file_name_list[0]))

        cropped = img.crop((x1*float(img.size[0]), y1*float(img.size[1]), x2*float(img.size[0]), y2*float(img.size[1])))  # (left, upper, right, lower)

        split_img = "split_" + file_name_list[0]

        split_img_dir = os.path.join("/home/lyx/django/test_upload/static/images",split_img)

        cropped.save(split_img_dir)

        od_lyx.main(split_img_dir)#OD

        ff=open(r'/home/lyx/django/test_upload/static/images/1.txt','r')
        result = ff.read()
        ff.close()

    return HttpResponse(result)#tode:result file name(dir)