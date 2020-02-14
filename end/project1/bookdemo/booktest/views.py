from django.shortcuts import render, redirect, reverse
from django.template import loader
from .models import Book, Hero
# Create your views here.

# MVT 中的V 视图模块
# 在此处接收请求 处理数据 返回响应

# 3.编写对应的视图函数
from django.http import HttpResponse, HttpResponseRedirect


def index(resquest):
    # return HttpResponse("这里是<h1>首页<h1>")
    # 1.获取模板
    # template = loader.get_template('index.html')
    # 2.渲染模板数据
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # 3.将渲染结果使用httpperponse返回
    # return HttpResponse(result)

    # 三合一
    return render(resquest, 'index.html', {"books": books})


def detail(resquest, bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(resquest, 'detail.html', {"book": book})


def about(resquest):
    return HttpResponse("这里是关于")


def deletebook(resquest, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # 删除一本书之后 仍然回到列表页
    # return HttpResponseRedirect(redirect_to='/')
    # 在view中解除硬编码
    url = reverse("booktest:index")
    return redirect(to=url)


def deletehero(resquest, heroid):
    hero = Hero.objects.get(id=heroid)
    # 一定要先获取 再删除
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)


def addhero(resquest, bookid):
    if resquest.method == "GET":
        return render(resquest, 'addhero.html')
    elif resquest.method == "POST":
        hero = Hero()
        hero.name = resquest.POST.get("heroname")
        hero.content = resquest.POST.get("herocontent")
        hero.gender = resquest.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)


def addbook(resquest):
    if resquest.method == "GET":
        return render(resquest, 'addbook.html')
    elif resquest.method == "POST":
        book = Book()
        book.title = resquest.POST.get("booktitle")
        book.price = resquest.POST.get("bookprice")
        book.pub_date = resquest.POST.get("pub_date")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)


def edithero(resquest, heroid):
    hero = Hero.objects.get(id=heroid)
    # 使用get方法进入英雄的编辑页面
    if resquest.method == "GET":
        return render(resquest, 'edithero.html', {"hero": hero})
    elif resquest.method == "POST":
        hero.name = resquest.POST.get("heroname")
        hero.content = resquest.POST.get("herocontent")
        hero.gender = resquest.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return redirect(to=url)


def editbook(resquest, Bookid):
    book = Book.objects.get(id=Bookid)
    if resquest.method == "GET":
        return render(resquest, 'editbook.html', {"book": book})
    elif resquest.method == "POST":
        book.title = resquest.POST.get("booktitle")
        book.price = resquest.POST.get("bookprice")
        book.pub_date = resquest.POST.get("pub_date")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)
# 使用Django 模板

# MVT
