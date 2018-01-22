from django.shortcuts import render

# Create your views here.
from django.http import Http404,HttpResponse,StreamingHttpResponse
from django.template import Template,Context
from django.shortcuts import render
import os


dict_path=r"/opt/logs/quickloan"
def list_log(request):
    show_path = r'loglist'
    # file_directory = os.path.join(os.getcwd(), show_path).replace('\\', '/')
    files = [name for name in os.listdir(dict_path) if
             os.path.isfile(os.path.join(dict_path, name))]
    #files = os.listdir(file_directory)
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


