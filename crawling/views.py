from django.shortcuts import render, redirect

from .models import Taling
from .crawling_module import taling_crawling

# Create your views here.

def crawling(request):
    keyword = request.POST['keyword']
    taling_data_list = taling_crawling(keyword)
    Taling.objects.all().delete()
    for i in range(len(taling_data_list)):
        Taling(
            title = taling_data_list[i][0],
            author = taling_data_list[i][1],
            price = taling_data_list[i][2],
            location = taling_data_list[i][3],
            link = taling_data_list[i][4],
        ).save()
    return redirect('study_list')
