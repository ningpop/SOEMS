from django.db import models
from user.models import User

# Create your models here.
class Study(models.Model):
    title = models.CharField(max_length = 50) # 강의 이름
    category = models.CharField(max_length = 50) # 강의 카테고리 (입력 시 ,로 구분할 것 ex. html, css, js)
    host = models.ForeignKey("user.User", on_delete=models.CASCADE) # 강의 진행자
    pub_date = models.DateField() # 강의 글 작성일자
    period = models.CharField(max_length=20) # 간단한 기간 (ex. 4주 과정)
    start_date = models.DateField() # 강의 시작 일자
    end_date = models.DateField() # 강의 종료 일자
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
    applicant = models.ForeignKey("user.User", on_delete=models.CASCADE, blank=True) # 강의 수강신청자

    def __str__(self):
        return self.study.title + " / " + self.applicant.name


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 작성자
    study = models.ForeignKey("Study", on_delete=models.CASCADE) # 해당 강의 글
    pub_date = models.DateTimeField(auto_now = True) # 댓글 작성 일자
    content = models.TextField() # 댓글 내용

    def __str__(self):
        return self.username.name
    