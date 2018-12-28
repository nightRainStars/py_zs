from django.shortcuts import render

# Create your views here.
from django.views import View

from recruit.models import Recruit


class RecruitView(View):
    def get(self, requset):
        recruit_all = Recruit.objects.all()

        return render(requset, 'job.html', {
            'recruit_all': recruit_all
        })
