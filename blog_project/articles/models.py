from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        #refrence to auth_user_model in settings(user.customuser)
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title