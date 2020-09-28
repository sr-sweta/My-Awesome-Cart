#I have created this
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index2.html')

def analyzed(request):
    ab=request.POST.get('text','default')
    b=request.POST.get('analyzed','off')
    dj=request.POST.get('counter','off')
    punc="""
    []{}-!"#$%&'()*+,./:;<=>?@\^_`|\
    """
    rem=""
    k=0
    if b == "on":
        for char in ab:
            if char not in punc:
                rem=rem+char
        params={'name':'Harry Bhai','place':rem,'char':k}
        ab=rem
    if dj == "on":
        for char in ab:
            k=k+1

        params={'name':'Harry Bhai','place':rem,'char':k}
        
    else:
        return HttpResponse("ERROR")

    return render(request,'analyze2.html',params)