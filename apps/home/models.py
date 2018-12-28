# encoding: utf-8
from datetime import datetime

from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class Video(models.Model):
    video_url = models.URLField(verbose_name='首页视频', max_length=200)
    video_bg = models.ImageField(verbose_name='视频背景', upload_to='video_bg/%Y/%m', default='video_bg/bg-1.png')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '首页视频'


class CompanyInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='公司名字')
    detail = UEditorField(verbose_name="公司详情", width=1200, height=300, imagePath="home/ueditor/",
                          filePath="home/ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '公司简介'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}简介'.format(self.name)


