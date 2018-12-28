from datetime import datetime

from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class Recruit(models.Model):
    recruit_name = models.CharField(max_length=100, verbose_name='职位')
    recruit_term = UEditorField(verbose_name="任职要求", width=1200, height=300, imagePath="recruit/ueditor/",
                                filePath="recruit/ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '招贤纳士'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.recruit_name
