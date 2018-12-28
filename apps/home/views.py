import json

from django.http import HttpResponse
from django.shortcuts import render

from home.models import Video, CompanyInfo
from news.models import News

__author__ = 'zhangzhen'
__date__ = '2018/12/26'
# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        videos = Video.objects.all()[:1][0]
        compang_info = CompanyInfo.objects.all()[:2]
        news = News.objects.all().order_by('-add_time')[:2]

        return render(request, 'index.html', {
            'videos': videos,
            'compang_info': compang_info,
            "news": news
        })


class ChangeImgsView(View):
    def get(self, request):
        news_infos = News.objects.all()
        status = request.GET.get('status', 0)
        print(status)
        news_info = [{'title': item.title, 'img_url': str(item.img_cover)} for item in news_infos]

        return HttpResponse(
            json.dumps(news_info),
            content_type='application/json')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
