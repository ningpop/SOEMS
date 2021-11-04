from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.study_list, name='study_list'),
    path('detail/<int:study_id>/', views.study_detail, name='study_detail'),
]
