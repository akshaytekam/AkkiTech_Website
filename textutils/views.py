'''
Text analyzer website with templates
'''
from django.http import HttpResponse
from django.shortcuts import render

def index(request):                               #Home index page
    return render(request, 'index.html')

def analyze(request):                              #Method for all variables
    #get the text using POST method
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('analyze', 'off')
    caps = request.POST.get('caps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on" and (len(djtext)>0):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if caps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized Text is:', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line:', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif charcount == "on":
        count = 0
        for char in djtext:
            if char != "\n":
                count = len(djtext)
        params = {'purpose': 'Char count is:', 'analyze_text': count}

    if (removepunc !="on" and caps !="on" and newlineremover !="on" and charcount !="on"):
        return HttpResponse("Error hai Bhai Please select the operations.")

    return render(request, 'analyze.html', params)

