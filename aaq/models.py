from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    tags = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    answered_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

