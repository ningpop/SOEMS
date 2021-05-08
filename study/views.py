from django.shortcuts import render

# Create your views here.

def study_list(request):
    return render(request, 'study_list.html')

def study_detail(request):
    return render(request, 'study_detail.html')