from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    GENDERTYPE_MALE = "남성"
    GENDERTYPE_FEMALE = "여성"

    GENDERTYPE_CHOICES = (
        (GENDERTYPE_MALE, "남성"),
        (GENDERTYPE_FEMALE, "여성"),
    )

    #profile_photo = models.ImageField() # 프로필 사진
    name = models.CharField(max_length = 100, null = False) # 이름
    email = models.CharField(max_length = 50)  # 이메일
    gender = models.CharField(max_length = 10, choices = GENDERTYPE_CHOICES) # 성별
    phone = models.CharField(max_length = 15) # 휴대폰 번호
    is_subscribe = models.BooleanField(default = False) # 구독 유무(강의 수강 가능/불가능 판단)
    subscribe_period = models.CharField(max_length = 50) # 구독 마감 날짜 -> datefield로 바꾸는거 찾아보기(not null이 안된대...)
    #subscribe_period = models.DateField(blank = True) # 구독 마감 날짜
    #description = models.TextField() # 이력

    def __str__(self):
        return self.name