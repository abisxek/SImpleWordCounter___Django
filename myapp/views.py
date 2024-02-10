from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'name':'Abi',
        'age':21
    }
    #name='Abi'
    return render(request,'index.html',context)
    #return HttpResponse('<h1>Hey there!</h1>')
    #return render(request, 'personal/home.html')
    #the first parameter is the request and the second is the template file
    # you direcly cant put html code/file into it and instead we create a template file
    #so we configure django to be able to look for the html files
    # we dont need to use hhtp response anymore, instead we use render
    #to make the code dynamic, we can pass a dictionary to the renfer function as a third parameter
    #if we are using a database, we do user.name to make it more dynamic
    # to make it formatted, we replace namee with context which is a dictionary containing different variables
def counter(request):
    text= request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html',{'amount': amount_of_words})