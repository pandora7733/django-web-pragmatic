from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # on_delete=models.CASCADE를 사용하면 사용자 삭제시 게시글도 함께 삭제됨
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)  # on_delete=models.CASCADE를 사용하면 사용자 삭제시 게시글도 함께 삭제됨

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)


