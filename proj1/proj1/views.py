from django import http
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse("About!")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('uppercase','off')
    newline=request.POST.get('newline','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    analyzed=""
    if removepunc=='on':
        punctuations='''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        # print(analyzed)
    if fullcaps=='on':
        if analyzed=="":
            for i in djtext:
                analyzed+=i.upper()
        else:
            any=""
            for i in analyzed:
                any+=i.upper()
            analyzed=any
    if newline=='on':
        if analyzed=="":
            for i in djtext:
                if i!='\n':
                    analyzed+=i
        else:
            any=""
            for i in analyzed:
                if i!='\n':
                    any+=i
            analyzed=any
    if spaceremover=='on':
        if analyzed=="":
            for i in djtext:
                if i!=' ':
                    analyzed+=i
        else:
            any=""
            for i in analyzed:
                if i!=' ':
                    any+=i
            analyzed=any
    if charcount=='on':
        count=0
        if analyzed=="":
            analyzed=djtext
            count=len(djtext)
        else:
            count=len(analyzed)
        analyzed=analyzed+' -- number of characters is'
        analyzed+=' '+str(count)

    else:
        return HttpResponse(analyzed)
    
    params={'purpose':'remove punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',params)
