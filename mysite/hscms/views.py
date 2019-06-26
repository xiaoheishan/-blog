from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from hscms.models import Userinfo
from myblog.models import Aritical
from myblog.forms import Aritical_Form

# Create your views here.
def index(request):
    if not isinstance(request.user,User):
        return redirect(to='myblog_index')

    userid = request.user
    print(userid)
    userinfo = Userinfo.objects.get(belong=userid)
    print(userinfo)
    context ={
        'userinfo':userinfo,
    }
    return render(request,'hscms/index.html',context)

# 文章列表

def list(request):
    if not isinstance(request.user,User):
        return redirect(to='myblog_index')
    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)

    artical = Aritical.objects.all()
    context = {
        'userinfo': userinfo,
        'artical': artical
    }
    return render(request,'hscms/list.html',context)

# 发布文章
def fabu(request):
    if not isinstance(request.user,User):
        return redirect(to='myblog_index')
    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    if request.method == 'GET':
        form = Aritical_Form
    if request.method == 'POST':
        form = Aritical_Form
        title = request.POST['title']
        print(title)
        content = request.POST['bar']
        print(content)
        img = request.FILES['suolvetu']
        print(img)
        new_artical = Aritical(title=title, content=content,img=img)
        new_artical.save()
        return redirect('/hsadmin/list')
    context = {
        'userinfo': userinfo,
        'form': form,
    }
    return render(request,'hscms/fabu.html',context)

#删除文章
def delete_artical(request,id):
    artical = Aritical.objects.get(id=id)
    print(artical)
    artical.delete()
    return redirect('/hsadmin/list')


# 文章内容
def artical(request,id):
    if not isinstance(request.user,User):
        return redirect(to='myblog_index')
    userid = request.user
    userinfo = Userinfo.objects.get(belong=userid)
    # 获取文章
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
        'userinfo': userinfo,
        'artical': artical,
    }
    return render(request,'hscms/artical.html',context)
