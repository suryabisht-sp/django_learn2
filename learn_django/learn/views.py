import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from learn.models import Myapp

def home_render(request):
    serviceData=Myapp.objects.all()
    for a in serviceData:
        print(a)
    return render(request,'home.html', {"data": serviceData})

def tset_render(request):
    response = requests.get('https://dummyjson.com/products')   
    if response.status_code == 200:
    # Parse the JSON response
        products_data = response.json()
    # Print the data
        context ={"data":products_data['products']}
        # print(context)
        return render(request,'tset.html', context=context)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return render(request,'tset.html')

def getName(request):
    name = "Surya"
    response = requests.get('https://dummyjson.com/products')   
    products_data = response.json()
    return JsonResponse(products_data, safe=False)

def about(request):
    return render (request, "about.html")

def coursedetail(request,coursedetail):
    return HttpResponse(coursedetail)

def submitfrm(request):
    return render(request, "submitfrm.html", {"data":request.POST})

def userForm(request):
    result={}
    try:
    #    name= request.GET["name"]
    #    email= request.GET["email"]
    #    message= request.GET["message"]
       name= request.POST["name"]
       email= request.POST["email"]
       message= request.POST["message"]
       result={"Name":name, "Email": email, "Message":message}
       return HttpResponseRedirect("/ch")
    except:
        pass
    return render(request, "userForm.html", {"output": result})

# def getName(request):
#     name = "Surya"
#     response = requests.get('https://dummyjson.com/products')   
#     products_data = response.json()
#     return Response(data=products_data )

# class Home(APIView):
#   def get(self,request):
#     return render(request,'home.html')
