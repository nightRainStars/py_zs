import xadmin
from recruit.models import Recruit


class RecruitAdmin(object):
    list_display = ['recruit_name', 'recruit_term', 'add_time']
    search_fields = ['recruit_name', 'recruit_term']
    list_filter = ['recruit_name', 'recruit_term', 'add_time']
    # 富文本
    style_fields = {"recruit_term": "ueditor"}


# 将管理器与model进行注册关联
xadmin.site.register(Recruit, RecruitAdmin)
