from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
#用户管理
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

from myblog.models import Topmenu,Banner

class TopmenuXuliehua(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Topmenu
        fields = '__all__'

class BannerData(serializers.ModelSerializer):
    class Meta:
        depin = 1
        model = Banner
        fields = '__all__'

@api_view(['GET','POST'])
def indexData(request):
    #首页的导航栏
    topmenu = Topmenu.objects.all()
    topmenuData = TopmenuXuliehua(topmenu,many=True)
    #首页的Banner
    banner = Banner.objects.all()
    bannerData = BannerData(banner,many=True)

    userid = request.user.id
    loginType = 'no'
    print(userid)
    if userid != None:
        loginType = 'ok'


    if request.method == 'POST':
        # print('ok')
        # post来的信息是什么
        username = request.POST['username']
        password = request.POST['password']
        # 验证这些信息是否通过了User login
        user = authenticate(username=username,password=password)
        print(user)
        if user != None:
            login(request,user)
            return Response({'loginType':'ok'})
    return Response({'topmenu': topmenuData.data, 'banner':bannerData.data,\
                     'loginType':loginType})