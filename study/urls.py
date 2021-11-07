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
]
