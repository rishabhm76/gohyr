from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import docx
import pdfplumber

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
        
        if files[f].name.endswith('.docx'):
            doc = docx.Document(files[f])
            text = ""
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
                text = '\n'.join(fullText)
        
            newFile['fileName'] = files[f].name
            newFile['content'] = text
                
        elif files[f].name.endswith('.pdf'):
            text = ""
            fullText = []
            with pdfplumber.open(files[f]) as pdf:
                for page in pdf.pages:
                    fullText = page.extract_text()
                    text += '\n' + fullText
                
            newFile['fileName'] = files[f].name
            newFile['content'] = text
            
        else:
            
            newFile['fileName'] = files[f].name
            newFile['content'] = files[f].read().decode("utf-8")
            fileList.append(newFile)
                  
        
    #print(x)
    return fileList
