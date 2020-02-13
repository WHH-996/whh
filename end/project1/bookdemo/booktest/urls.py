# author: WH
# date: 2020/2/13 14:35
# 引入路由绑定函数
from django.conf.urls import url
from . import views

# 2.每个路由文件中必须编写路由数组
urlpatterns = [
    url(r'^index/$', views.index),
    # 使用正则分组可以向视图函数中传递参数
    # 第一个参数就是路由 第二个参数就是视图
    # 第一个参数如果有正则参数 小括号 则正则分组匹配内容会作为实参传递给视图函数
    url(r'^detail/(\d+)/', views.detail),
    url(r'^about/$', views.about),
]
