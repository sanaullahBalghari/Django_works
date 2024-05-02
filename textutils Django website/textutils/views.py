
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   
    return render(request,'index2.html')
    # return HttpResponse("home")

def analyze(request):
    djtext=request.POST.get('text','default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    charcount=request.POST.get('charcount','off')
    space_remover=request.POST.get('space_remover','off')
    newlineremover=request.POST.get('newlineremover','off')
   


    if removepunc=="on":
        # analyzed=djtext
        punctuations='''. , ; : ? ! ' " - ( ) [ ] ... / \ ~ ` @ # $ % ^ & * _ + = < > | { }'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html',params)
           
    if(fullcaps == "on"):
        analyzed= ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'purpose':'changed to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html',params)
    if( charcount == "on"):
        analyzed= 0
        for char in djtext:
            analyzed=analyzed + len(char) 
        params={'purpose':'character count','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html',params)
    if( space_remover == "on"):
        analyzed= ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index +1] == " "):
                analyzed=analyzed + char
        params={'purpose':'newlineremover','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze2.html',params)
    if( newlineremover== "on"):
        analyzed= ""
        for char in djtext:
            if char !="\n"  and char!="\r":
                analyzed=analyzed + char
        #     else:
        #         print("no")
        # print("pre", analyzed)
        params={'purpose':'newlineremover','analyzed_text':analyzed}
        djtext=analyzed
    # return render(request, 'analyze2.html',params)
    # if(removepunc!="on" and fullcaps != "on" and charcount!= "on" and space_remover!= "on"):
    #     return HttpResponse("Error")
    
    return render(request, 'analyze2.html',params)






    
