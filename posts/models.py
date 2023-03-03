from django.db import models
from user.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']


    def __str__(self):
        return self.title
