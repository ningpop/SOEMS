from django.shortcuts import render
from .models import Study

# Create your views here.

def study_list(request):
    study_query_set = Study.objects.order_by('pub_date')
    context = { 'studies' : study_query_set }
    return render(request, 'study_list.html', context)

def study_detail(request, study_id):
    study = Study.objects.get(pk=study_id)
    category = study.category.split(',')
    context = {
        'study' : study,
        'categories' : category
        }
    return render(request, 'study_detail.html', context)