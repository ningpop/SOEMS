from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.study_list, name='study_list'),
    path('detail/<int:study_id>/', views.study_detail, name='study_detail'),
    path('create/', views.study_create, name='study_create'),
    path('update/<int:study_id>/', views.study_update, name='study_update'),
]
