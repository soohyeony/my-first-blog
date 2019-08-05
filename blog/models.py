from django.db import models
from django.utils import timezone

#모델(객체)을 정의(class로 선언), 클래스의 첫글자를 항상 대문자로 써야한다.
class Post(models.Model):
    #속성정의
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #models.CharFeild() : 글자수가 제한된 텍스트를 정의, 제목
    text = models.TextField() #m글자수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField( #날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField( #다른 모델에 대한 링크
            blank=True, null=True)

    def publish(self):  #publish 메서드(def로 선언):소문자와 언더스코어로 네이밍
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #__str__메서드 : 제목 텍스트를 리턴
        return self.title