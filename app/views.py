from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import User, news, Staff, ProDuct, Casedb, ChatT
from project import settings


def index(request):
    t = news.objects.all()
    a = []
    for i in t:
        a.append(i)
    if len(a) > 10:
        a = a[-10:]
    c = ProDuct.objects.all()
    if len(c) > 6:
        b = A(c[:7]) if len(A(c[:7])) > 1 else [c[:7], ]
    else:
        b = A(c) if len(A(c)) > 1 else [c, ]
    return render(request, 'index.html', locals())


def index2(request):
    a = news.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


# 新闻中心
def new(request):
    n = news.objects.all()
    return render(request, 'new.html', locals())


def product(request):
    a = ProDuct.objects.all()
    b = A(a) if len(A(a)) > 1 else [a, ]
    return render(request, 'product.html', locals())


def A(l):
    import math
    p = len(l)
    if p > 3:
        c = math.ceil(p / 3)
        i = 0
        a = [[] for i in range(c)]
        for f in a:
            for q in range(3):
                try:
                    f.append(l[i])
                    i += 1
                except:
                    break
        return a
    else:
        return [l, ]


def case(request):
    a = Casedb.objects.all()
    b = A(a) if len(A(a)) > 1 else [a, ]
    return render(request, 'case.html', locals())


def contact(request):
    a = Staff.objects.all()
    b = A(a) if len(A(a)) > 1 else [a, ]
    return render(request, 'contact.html', locals())


from django.views.decorators.csrf import csrf_exempt


# #登录
@csrf_exempt
def login1(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
        else:
            return HttpResponse('<script>alert("账号或者密码不正确");window.history.back(-1);  </script>')
        return redirect('index')
    return render(request, 'login3.html', locals())


# 退出
def do_logout(request):
    logout(request)
    return redirect('index')


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        telephone = request.POST.get('telephone', None)
        if username and password and telephone and len(telephone) == 11:
            # try:
            user = User.objects.create_user(username=username, password=password, telephoneNmuber=telephone)
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponse('<script>alert("注册成功，即将返回。");window.location.replace("/");;  </script>')
            # except:
            #     return HttpResponse('<script>alert("用户名或者号码已经存在，即将返回。");window.history.back(-1);  </script>')
        else:
            return HttpResponse('<script>alert("注册失败，即将返回。");window.history.back(-1);  </script>')
    return render(request, 'register.html', locals())


def text(request):
    if request.GET.get('a'):
        c = news.objects.get(id=request.GET.get('a'))
    return render(request, 'text.html', locals())


def test(request):
    a = Casedb()
    a.name = 'ojbk'
    a.image = '/static/case/timg.jpeg'
    a.detailed = '''    又一次站在那个演讲台上，又一次处于紧张焦虑之中，可一个淡淡的微笑却让自己平静下来，不仅给自己足够的信心，而且也给别人带来永恒的温馨，只因为相信我能行。再说就算成又怎样，败又怎样，一个微笑，一切都将过去，只想将一个自信的微笑留给自己，留给未来。想想古今中外又有哪个名人伟人没有经历过失败呢?可他们在失败面前都选择了给自己一个自信的微笑，邓亚萍选择了微笑，邰丽华选择了微笑，海伦凯勒选择了微笑，张海迪也选择了微笑是自信给了我微笑，也是微笑给了我自信。
宽容微笑
　　在公共汽车上，不小心踩到了别人的脚，一个淡淡的微笑包含了满怀歉意，包含了一声简单的对不起，一切尽在不言中，谁说只有眼睛才是心灵的窗户，微笑也是心灵的另一扇窗。而当自己被别人不小心踩到脚时，也向别人投去一个淡淡的微笑，这是一声真诚的没关系，消除了对方的恐惧，换得的也是别人的微笑，礼尚往来嘛!用微笑去面对别人的暴力，以静制动，以微笑战胜暴力，让他们自己感到惭愧。微笑既提高了自己的修养又帮助了别人，这才是宽容的微笑之真谛!是宽容教会了我微笑，也是微笑教会了我宽容。
　　在4年前的那次全县小学生运动会上，当一个朝气蓬勃的女孩稳稳地高举着校牌穿过整个会场时，她洋溢着一脸的微笑，她的全身都焕发着青春的气息，那是一种微笑之美，是一种任何事物都无法替代的美，是一种超然物外的美。那种美来自一颗真心，一颗纯洁之心，来自一种热爱，对母校的热爱。真诚的微笑、鼓励的微笑、快乐的微笑这些都是美丽的微笑。是这个世界让微笑更加灿烂，也是微笑让世界更加美丽。
　　也许在我们的一生中，会遇到很多的烦心事，考试不及格、愿望不能实现、目标达不到可如果没有这些，用傅雷的话说：做人也就太腻了。再说了就算我们愁眉苦脸甚至痛哭一声，发泄一次，这些都无济于事。而我们应该做的是想好如何面对未来，还有一年，我们将走进中考的考场，还有一年，我们将踏进高中的殿堂，还有一年，我们将放飞理想的翅膀!还有一年，不!只剩一年了，我们不能再了，振作起来吧!让我们用自信的微笑、宽容的微笑、美丽的微笑所形成的更加灿烂的微笑面对挫折、面对失败、面对不幸、面对生活中一切的绊脚石。让我们一起将嘴角轻轻上扬!t'''
    # a.one = models.CharField(max_length=256, verbose_name='特点1')
    # a.two = models.CharField(max_length=256, verbose_name='特点2')
    # a.there = models.CharField(max_length=256, verbose_name='特点3')
    # a.four = models.CharField(max_length=256, verbose_name='特点4')
    # a.five = models.CharField(max_length=256, verbose_name='特点5')
    a.save()
    return HttpResponse('ok')


def test1(request):
    a = request.GET.get('a', None)
    a = Staff.objects.get(id=a)
    return render(request, '123456.html', locals())


def productsite(request):
    a = request.GET.get('a', None)
    v = ProDuct.objects.get(id=a)
    return render(request, 'productsite.html', locals())


def casesite(request):
    a = request.GET.get('a', None)
    b = Casedb.objects.get(id=a)
    return render(request, 'casesite.html', locals())


p = []

import time


@login_required(login_url='/qlogin/')
def Chat(request):
    a = ChatT.objects.all().order_by('-id')
    if request.method == "POST":
        r = request.POST.get('text', None)
        q = request.POST.get('issuper', None)
        if q:
            ChatT.objects.create(text=r, uid=User.objects.get(id=q), issuper=1)
            return HttpResponse('ok')
        if r:
            ChatT.objects.create(text=r, uid=request.user, issuper=0)
            return HttpResponse('ok')
    #     q = request.POST.get('text', None)
    #     # if q == 'vIp人员在线':
    #     ChatT.objects.create(text=q,issuper=0,uid=request.user.id,userne=request.user.username)
    #         # return
    #     return
    # if request.method == "PUT":
    #     ChatT.objects.filter(uid=request.user.id,userne=request.user.username,issuper=1)
    #     return HttpResponse()

    return render(request, 'liuyanban.html', locals())


from django.views.generic import View


class ta(View):
    def put(self, request, *args, **kwargs):
        return 1

    def get(self, request, *args, **kwargs):
        return render(request, 'tahc.html', locals())

    def post(self, request, *args, **kwargs):
        time.sleep(2)
        q = request.POST.get('id', None)
        ChatT.objects.get(id=q).delete()
        return HttpResponse(1)


from .Formq import UserForm, product_Form, qweqwe


def upload(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)  # 还没有查到是什么意思
        # 判断是否为有效的
        if uf.is_valid():
            # 获取表单元素
            title = uf.cleaned_data['title']
            # text = uf.cleaned_data['text']
            # print(title,text)

            pic = request.FILES.get('text')  # 'pic'对应前端表单的name属性值。

            # 2.创建一个文件(用于保存图片)
            save_path = '%s/pdf/%s' % (settings.MEDIA_ROOT, pic.name)  # pic.name 上传文件的源文件名
            with open(save_path, 'wb') as f:
                # 3.获取上传文件的内容并写到创建的文件中
                for content in pic.chunks():  # pic.chunks() 上传文件的内容。
                    f.write(content)

            # 4.在数据库中保存上传记录
            # 写入数据库
            nw = news()
            nw.title = title
            nw.text = '/static/pdf/%s' % pic.name
            nw.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
        # 返回一个空表单
    return render(request, 'upload.html', {'uf': uf})


def delete_news(request):
    a = request.GET.get('a', None)
    if a:
        news.objects.get(id=a).delete()
    return redirect('new')

def  case_upload(request):
    if request.method == "POST":
        uf = product_Form(request.POST, request.FILES)  # 还没有查到是什么意思
        # 判断是否为有效的
        if uf.is_valid():
            # 获取表单元素
            name = uf.cleaned_data['name']
            detailed = uf.cleaned_data['detailed']

            # text = uf.cleaned_data['text']
            # print(title,text)
            pic = request.FILES.get('P_image')  # 'pic'对应前端表单的name属性值。

            # 2.创建一个文件(用于保存图片)
            save_path = '%s/case/%s' % (settings.MEDIA_ROOT, pic.name)  # pic.name 上传文件的源文件名
            with open(save_path, 'wb') as f:
                # 3.获取上传文件的内容并写到创建的文件中
                for content in pic.chunks():  # pic.chunks() 上传文件的内容。
                    f.write(content)

            # 4.在数据库中保存上传记录
            # 写入数据库
            nw = Casedb()
            nw.name = name
            nw.image = '/static/case/%s' % pic.name
            nw.detailed = detailed
            nw.save()

            return HttpResponse('upload ok!')
    else:
        uf = product_Form()
        # 返回一个空表单
    return render(request, 'case_upload.html', {'uf': uf})

def delete_case(request):
    a = request.GET.get('a', None)
    if a:
        Casedb.objects.get(id=a).delete()
    return redirect('case')

def  product_upload(request):
    if request.method == "POST":
        uf = product_Form(request.POST, request.FILES)  # 还没有查到是什么意思
        # 判断是否为有效的
        if uf.is_valid():
            # 获取表单元素
            name = uf.cleaned_data['name']
            detailed = uf.cleaned_data['detailed']
            trait_one = request.POST.get('trait_one')
            trait_two = request.POST.get('trait_two')
            trait_there = request.POST.get('trait_there')
            trait_four = request.POST.get('trait_four')
            trait_five = request.POST.get('trait_five')
            # text = uf.cleaned_data['text']
            # print(title,text)
            pic = request.FILES.get('P_image')  # 'pic'对应前端表单的name属性值。

            # 2.创建一个文件(用于保存图片)
            save_path = '%s/product/%s' % (settings.MEDIA_ROOT, pic.name)  # pic.name 上传文件的源文件名
            with open(save_path, 'wb') as f:
                # 3.获取上传文件的内容并写到创建的文件中
                for content in pic.chunks():  # pic.chunks() 上传文件的内容。
                    f.write(content)

            # 4.在数据库中保存上传记录
            # 写入数据库
            nw = ProDuct()
            nw.name = name
            nw.P_image = '/static/product/%s' % pic.name
            nw.detailed = detailed
            nw.trait_one = trait_one
            nw.trait_two = trait_two
            nw.trait_there = trait_there
            nw.trait_four = trait_four
            nw.trait_five = trait_five
            nw.save()
            return HttpResponse('upload ok!')
    else:
        uf = qweqwe()
        # 返回一个空表单
    return render(request, 'product_upload.html', {'uf': uf})

def delete_product(request):
    a = request.GET.get('a', None)
    if a:
        ProDuct.objects.get(id=a).delete()
    return redirect('product')