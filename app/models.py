from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telephoneNmuber = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username


import django.utils.timezone as timezone


class news(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    date_publish = models.DateField(default=timezone.now, verbose_name='上传时间')
    text = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=128, verbose_name='员工名')
    telephone = models.CharField(max_length=11,verbose_name='电话号码')
    wechat = models.CharField(max_length=128, verbose_name='微信账号')
    qq = models.CharField(max_length=10,verbose_name='qq号码')
    email = models.CharField(max_length=128, verbose_name='邮箱')
    head = models.CharField(max_length=512,verbose_name='头像路径')

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

class ProDuct(models.Model):
    name = models.CharField(max_length=128,verbose_name='产品名称')
    P_image = models.CharField(max_length=256,verbose_name='产品图样')
    detailed = models.TextField(verbose_name='详细说明')
    trait_one = models.CharField(max_length=256,verbose_name='特点1')
    trait_two = models.CharField(max_length=256,verbose_name='特点2')
    trait_there = models.CharField(max_length=256,verbose_name='特点3')
    trait_four = models.CharField(max_length=256,verbose_name='特点4')
    trait_five = models.CharField(max_length=256,verbose_name='特点5')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural =verbose_name
        ordering = ['id']
    def __str__(self):
        return self.ordering

class Casedb(models.Model):
    name = models.CharField(max_length=128,verbose_name='产品名称')
    image = models.CharField(max_length=256,verbose_name='产品图样')
    detailed = models.TextField(verbose_name='详细说明')
    one = models.CharField(max_length=256,verbose_name='特点1')
    two = models.CharField(max_length=256,verbose_name='特点2')
    there = models.CharField(max_length=256,verbose_name='特点3')
    four = models.CharField(max_length=256,verbose_name='特点4')
    five = models.CharField(max_length=256,verbose_name='特点5')

    class Meta:
        verbose_name = '案例'
        verbose_name_plural =verbose_name
        ordering = ['id']
    def __str__(self):
        return self.name

class ChatT(models.Model):
     text = models.TextField(verbose_name='内容')
     issuper = models.IntegerField(verbose_name='是否为管理员发言')
     uid = models.ForeignKey('User',on_delete=models.CASCADE)
     userne = models.CharField(max_length=128,verbose_name='凭证')
     date_time = models.DateField(default=timezone.now, verbose_name='上传时间')
     class Meta:
         verbose_name = '聊天'
         verbose_name_plural = verbose_name
         ordering = ['id']

     def __str__(self):
         return self.uid