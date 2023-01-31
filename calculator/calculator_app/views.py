from email import message
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages

from calculator_app.models import calculator


def index(request):
    return render(request,'index.html')



def submitquery(request):
    q = request.POST['query']
    try:
        ans = eval(q)
        context= {
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True
        }
        calculator.objects.create(query=q,ans=ans)
        return render(request,'index.html',context)
    except:
        context= {
            "error" : True,
            "result" : False

        }
        return render(request,'index.html',context)

        


def history(request):
    history=calculator.objects.all()  
    context={
        "history":history
    }
    return render(request,'history.html',context)
    
    
def delete(request,pk):
    calculator.objects.filter(id=pk).delete()
    # try:     # if  request.method=='POST':
   
    # query.delete()
    # except IndexError:
    messages.success(request,("The calculation History was Deleted !"))
    return redirect('history') 
            # #     try: 
    #        del last_calculation[i]
    #     except IndexError:
    #         print(last_calculation)
    # # except IndexError:
    #     pass
    
        # context={
        #     "delete_text":"All History Is Deleted !"
        # }
        # return render(request,'history.html')
        # success_url=reverse_lazy('index')
    # message="All History Is Deleted !"
    