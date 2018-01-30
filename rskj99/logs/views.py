#-*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import Http404,HttpResponse,StreamingHttpResponse
from django.template import Template,Context
from django.shortcuts import render
import os
import collections
import time


dict_path=r"/opt/logs/quickloan"
def list_log(request):
    show_path = r'loglist'
    # file_directory = os.path.join(os.getcwd(), show_path).replace('\\', '/')
    files = [name for name in os.listdir(dict_path) if
             os.path.isfile(os.path.join(dict_path, name))]
    #files = os.listdir(dict_path) #包涵目录
    
    app_dict={}
    for app in files:
	app_info_dict = collections.OrderedDict()
	app_unix_time = os.stat(os.path.join(dict_path, app)).st_mtime
	app_create_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(app_unix_time))
	app_size = os.stat(os.path.join(dict_path, app)).st_size
	
	if app_size > 1024 * 1024:
            app_info_dict["app_size"] = "%.2fMB" % (app_size / 1024 / 1024)
        else:
            app_info_dict["app_size"] = "%.2fKB" % (app_size / 1024)

	app_info_dict["app_create_time"] = app_create_time
        app_dict[app] = app_info_dict

    app_dict = sorted(app_dict.items(), key=lambda item: item[1]["app_create_time"], reverse=True)
    return render(request, "logs.html", locals())

def download_log(request,logs_name):
    # do something...
    def file_iterator(file_name, chunk_size=8192):
        with open(os.path.join(dict_path,file_name)) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(logs_name)) #'Content-Type'='application/octet-stream')
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(logs_name)
    return response



tea_path=r"/opt/logs/tea"
def tea_log(request):
    show_path = r'tealog'
    # file_directory = os.path.join(os.getcwd(), show_path).replace('\\', '/')
    files = [name for name in os.listdir(tea_path) if
             os.path.isfile(os.path.join(tea_path, name))]
    app_dict={}
    for app in files:
        app_info_dict = collections.OrderedDict()
        app_unix_time = os.stat(os.path.join(tea_path, app)).st_mtime
        app_create_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(app_unix_time))
        app_size = os.stat(os.path.join(tea_path, app)).st_size

        if app_size > 1024 * 1024:
            app_info_dict["app_size"] = "%.2fMB" % (app_size / 1024 / 1024)
        else:
            app_info_dict["app_size"] = "%.2fKB" % (app_size / 1024)

        app_info_dict["app_create_time"] = app_create_time
        app_dict[app] = app_info_dict

    app_dict = sorted(app_dict.items(), key=lambda item: item[1]["app_create_time"], reverse=True)
    return render(request, "logs.html", locals())


def down_tealog(request,tealogs_name):
    # do something...
    def file_iterator(file_name, chunk_size=8192):
        with open(os.path.join(tea_path,file_name)) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(tealogs_name)) #'Content-Type'='application/octet-stream')
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(tealogs_name)
    return response
