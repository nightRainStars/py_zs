# encoding: utf-8

__author__ = 'zhangzhen'
__date__ = '2018/12/27'


from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models


# Create your models here.

class News(models.Model):
    img_cover = models.ImageField(verbose_name='封面', upload_to='news/%Y/%m', default='video_bg/bg-1.png')
    title = models.CharField(verbose_name='新闻标题', max_length=50)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    detail = UEditorField(verbose_name="新闻内容", width=1200, height=300, imagePath="news/ueditor/",
                          filePath="news/ueditor/", default='')

    class Meta:
        verbose_name = '公司动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.title)
