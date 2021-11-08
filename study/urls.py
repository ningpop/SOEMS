from django.urls import path, include
from . import views

urlpatterns = [
    # Study
    path('list/', views.study_list, name='study_list'),
    path('detail/<int:study_id>/', views.study_detail, name='study_detail'),
    path('create/', views.study_create, name='study_create'),
    path('update/<int:study_id>/', views.study_update, name='study_update'),
    path('delete/<int:study_id>/', views.study_delete, name='study_delete'),

    # Review
    path('review_create/<int:study_id>/', views.review_create, name='review_create'),
    path('review_delete/<int:study_id>/<int:review_id>/', views.review_delete, name='review_delete'),

    # Participation
    path('detail/<int:study_id>/participate_at_study', views.participate_at_study, name='participate_at_study'),
    path('detail/<int:study_id>/participate_cancel', views.participate_cancel, name='participate_cancel'),

    # Send Study link SMS
    path('detail/<int:study_id>/start_lecture', views.start_lecture, name='start_lecture'),
]
