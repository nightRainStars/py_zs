import xadmin
from news.models import News


class NewsAdmin(object):
    list_display = ['title', 'img_cover', 'detail', 'add_time']
    search_fields = ['title', 'img_cover', 'detail']
    list_filter = ['title', 'img_cover', 'detail', 'add_time']
    # 富文本
    style_fields = {"detail": "ueditor"}


# 将管理器与model进行注册关联
xadmin.site.register(News, NewsAdmin)
