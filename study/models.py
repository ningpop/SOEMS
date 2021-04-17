from django.db import models
from user.models import User

# Create your models here.
class Study(models.Model):
    title = models.CharField(max_length = 50) # 강의 이름
    category = models.CharField(max_length = 20) # 강의 카테고리
    host = models.ForeignKey("user.User", on_delete=models.CASCADE) # 강의 진행자
    pub_date = models.DateField() # 강의 글 작성일자
    start_period = models.DateField() # 강의 시작 일자
    end_period = models.DateField() # 강의 종료 일자
    hit_count = models.PositiveIntegerField(default = 0) # 강의 글의 조회수
    content = models.TextField() # 강의 글 내용
    #content_photos = models.ImageField() # 강의 글 내용 속 이미지
    #attechment = models.FileField(upload_to = '') # 첨부 파일
    total_people = models.PositiveSmallIntegerField() # 전체 모집 인원
    current_people = models.PositiveSmallIntegerField() # 현재 모집 인원

    def __str__(self):
        return self.title


class Participation(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE) # 해당 강의 글
    max_size = models.PositiveSmallIntegerField(default = 5) # 최대 인원 수
    applicant = models.ManyToManyField("user.User", blank = True) # 강의 수강신청자

    @property
    def is_full(self):
        return self.applicant.count() == self.max_size

class Review(models.Model):
    username = models.ForeignKey("user.User", on_delete=models.CASCADE) # 댓글 작성자
    study = models.ForeignKey("Study", on_delete=models.CASCADE) # 해당 강의 글
    pub_date = models.DateTimeField(auto_now = True) # 댓글 작성 일자
    content = models.TextField() # 댓글 내용

    def __str__(self):
        return self.username
    