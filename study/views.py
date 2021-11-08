from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Study, Review, Participation
import datetime

# Create your views here.

''' Study '''

def study_list(request):
    study_query_set = Study.objects.order_by('pub_date')
    context = { 'studies' : study_query_set }
    return render(request, 'study_list.html', context)

def study_detail(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    study.hit_count += 1
    study.save()
    category = study.category.split(',')
    did_participate = False
    participation = Participation.objects.filter(study=study, applicant=request.user)
    if participation.count() != 0:
        did_participate = True
    now = datetime.date.today()
    context = {
        'study' : study,
        'categories' : category,
        'did_participate' : did_participate,
        "now" : now
        }
    return render(request, 'study_detail.html', context)

@login_required
def study_create(request):
    if request.method == 'POST':
        study = Study()
        study.title = request.POST['title']
        study.category = request.POST['category']
        study.host = request.user
        study.pub_date = datetime.date.today()
        study.period = request.POST['period']
        study.start_date = request.POST['start_date']
        study.end_date = request.POST['end_date']
        study.content = request.POST['content']
        study.total_people = request.POST['total_people']
        study.current_people = 0
        study.save()
        this_study = get_object_or_404(Study, pk=study.id)
        context = {
            'study' : this_study
        }
        return render(request, 'study_detail.html', context)

    return render(request, 'study_create.html')

@login_required
def study_update(request, study_id):
    study = get_object_or_404(Study, pk=study_id)

    if request.method == 'POST':
        study.title = request.POST['title']
        study.category = request.POST['category']
        study.period = request.POST['period']
        study.start_date = request.POST['start_date']
        study.end_date = request.POST['end_date']
        study.content = request.POST['content']
        study.total_people = request.POST['total_people']
        study.save()
        return redirect("study_detail", study_id)

    context = {
        "study" : study
    }
    return render(request, "study_update.html", context)

@login_required
def study_delete(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    study.delete()
    return redirect("study_list")



''' Review '''

@login_required
def review_create(request, study_id):
    if request.method == 'POST':
        review = Review()
        review.study = get_object_or_404(Study, pk=study_id)
        review.username = request.user
        review.content = request.POST['content']
        review.pub_date = datetime.date.today()
        review.save()
        return redirect('study_detail', study_id)

@login_required
def review_delete(request, study_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.username:
        review.delete()
        return redirect('study_detail', study_id)
    raise PermissionDenied



''' 수강신청 '''

def participate_at_study(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    if study.start_date < datetime.date.today():
        return redirect('study_detail', study_id)
    if study.host != request.user:
        participation = Participation()
        participation.study = study
        participation.applicant = request.user
        participation.save()
    return redirect('study_detail', study_id)

def participate_cancel(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    participation = get_object_or_404(Participation, study=study, applicant=request.user)
    participation.delete()
    return redirect('study_detail', study_id)