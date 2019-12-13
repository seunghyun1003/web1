from django.db import models
from django.urls import reverse

# Create your models here.
class Entries(models.Model):
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "title: " + self.title + ", content : "+self.content

class Category(models.Model):
    name = models.CharField(max_length=50, help_text='글의 분류를 입력하세요.(ex: 간단한 메모)')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, help_text='글의 분류를 설정하세요.')

    def __str__(self):
        return self.title

    #1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    #content가 200자 이상?
    def is_content_more200(self):
        return len(self.content) > 200
    #300자가 넘어가면 200자까지만 출력
    def get_content_under200(self):
        return self.content[:200]
