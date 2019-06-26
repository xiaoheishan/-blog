from django.shortcuts import render,redirect
from .models import Topmenu,Aritical
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    topmenu = Topmenu.objects.all()

    artical = Aritical.objects.all()
    context = {
        'topmenu': topmenu,
        'artical': artical,
    }
    return render(request, 'myblog/index.html',context)

def chakan(request,id):
    artical = Aritical.objects.get(id=id)
    print(artical)

    if request.method == 'POST':
        title = request.POST['title']
        try:
            img = request.FILES['suolvetu']
            print(title)
        except:
            img = artical.img
        content = request.POST['content']
        print(title)
        print(img)
        print(content)
        artical.title = title
        artical.img = img
        artical.content = content
        artical.save()

    context = {
        'artical': artical,
    }
    return render(request,'myblog/chakan.html',context)
