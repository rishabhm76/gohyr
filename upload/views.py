from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.FILES)
        result = my_program(request.FILES)
        return JsonResponse(result, safe=False)
    return HttpResponse('Upload service up.....')
    # return render(request, "index.html")


def my_program(files):
    fileList = []
    for f in files.keys():
        newFile = {}
        newFile['fileName'] = files[f].name
        newFile['content'] = files[f].read().decode("utf-8")
        fileList.append(newFile)
    #print(x)
    return fileList