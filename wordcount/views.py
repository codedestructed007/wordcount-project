from django.http import HttpResponse
from django.shortcuts  import render

def frontpage(request):
    return render(request , 'frontpage.htm')

def count(request):
    mytext = request.GET['fulltext']
    words = mytext.split()
    worddictionary = {}
    for word in words:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1





    totallength = len(str(mytext))
    return render(request , 'count.htm'  , {'mytext': mytext , 'length' : totallength , 'worddictionary': worddictionary.items()})

def about(request):
    return render(request , 'about.htm' )