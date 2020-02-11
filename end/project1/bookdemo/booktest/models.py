from django.db import models


# Create your models here.

# MVT 数据模型
# OPM 数据模型
# 在此处编写应用的数据模型类
# 每一张表就是一个模型类
# 有了ORM之后我们就可以定义出表对应的模型类
# 通过操作模型类去操作数据库  不需要写sql语句

# 有了模型类怎么与数据进行交互
# 1.注册模型 在setting.py 中的INSTALLED_APPS添加应用名
# 2.生成迁移文件 用于与数据库的交互 Python manage.py makemigrations  会在对应的应用下方生成迁移文件 不需要关注
# 3.执行迁移 会在对应的数据库中生成对应的表 python manage.py migrate
# 模型类更改
class Book(models.Model):
    """
    book继承了Model类 因为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero继承了Model  也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book  是一对多中的外键  on_delete代表删除主表数据时数据如何做
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# django  orm关联查询
# 多方Hero  一方Book
# 1.多找一  多方对象.关系字段  exp:h1.book
# 2.一找多  一方对象,小写多放类名_set.all()  exp:b1.hero_set.all()
