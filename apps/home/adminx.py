import xadmin
from home.models import Video, CompanyInfo
from news.models import News
from recruit.models import Recruit
from xadmin import views


class VideoAdmin(object):
    list_display = ['video_url', 'video_bg', 'add_time']
    search_fields = ['video_url', 'video_bg']
    list_filter = ['video_url', 'video_bg', 'add_time']


class CompanyInfoAdmin(object):
    list_display = ['name', 'detail', 'add_time']
    search_fields = ['name', 'detail']
    list_filter = ['name', 'detail', 'add_time']
    # 富文本
    style_fields = {"detail": "ueditor"}


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "中思科技后台管理站"
    site_footer = "www.zhongsikeji.com"

    def get_site_menu(self):
        return (
            {'title': '我的后台', 'menus': (
                {'title': '首页视频', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '公司信息', 'url': self.get_model_url(CompanyInfo, 'changelist')},
                {'title': '公司动态', 'url': self.get_model_url(News, 'changelist')},
                {'title': '招贤纳士', 'url': self.get_model_url(Recruit, 'changelist')},
            )},
        )


# 将管理器与model进行注册关联
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CompanyInfo, CompanyInfoAdmin)

# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
