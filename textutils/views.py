from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    # get the text
    dj_text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,=<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in dj_text:
            analyzed+=char.upper()
        params = {'purpose':'Capitalizing the Text', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose':'Capitalizing the Text', 'analyzed_text': analyzed}
        dj_text = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(dj_text):
            if not(dj_text[index]==" " and dj_text[index+1]==" "):
                analyzed += char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("Error 404 : Please select at-least one operation and Try Again..!!!")

    return render(request, 'analyze.html', params)
