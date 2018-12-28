from django.core.paginator import PageNotAnInteger
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from pure_pagination import Paginator

from news.models import News


class NewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-add_time')

        # 分页功能
        try:
            page_num = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_num = 1
        # page_num = int(page_num)
        p = Paginator(news, 2, request=request)
        # news_p = p.page(page)
        news_p = p.page(page_num)

        return render(request, 'news.html', {
            'news': news_p
        })


class DetailView(View):
    def get(self, request, detail_id):
        try:
            new_detail = News.objects.get(id=detail_id)
        except News.DoesNotExist:
            raise Http404

        # 实现上一篇与下一篇功能

        id_prev = id_next = int(detail_id)
        next_detail = prev_detail = ''
        id_max = News.objects.all().order_by('-id').first().id
        while id_prev >= 1:
            next_detail = News.objects.filter(id=id_prev - 1).first()
            if not next_detail:
                id_prev -= 1
            else:
                break
        while id_next <= id_max:
            prev_detail = News.objects.filter(id=id_next + 1).first()

            if not prev_detail:
                id_next += 1
            else:
                break

        return render(request, 'news_details.html', {
            'new_detail': new_detail,
            'next_detail': next_detail,
            'prev_detail': prev_detail,
        })
