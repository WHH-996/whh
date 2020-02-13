from django.shortcuts import render
from django.template import loader
from .models import Book, Hero
# Create your views here.

# MVT 中的V 视图模块
# 在此处请求接收 处理数据 返回响应

# 3.编写对应的视图函数
from django.http import HttpResponse


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

# 使用Django 模板
# MVT
