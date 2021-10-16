from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from functools import partial
from nanoid import generate


class Project(models.Model):
    id = models.CharField(max_length=21, default=generate, primary_key=True, editable=False)
    domain = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)


class Thunder(models.Model):
    thunder_name = models.CharField(max_length=255)
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    details = models.TextField(null=True)

    def __str__(self):
        return '{}'.format(self.thunder_name)


class ThunderSupport(models.Model):
    statusCode = models.IntegerField(primary_key=True, editable=False)
    suggestion = models.TextField()
    rel_link = models.TextField()


class ThunderSource(models.Model):
    insecureCode = models.TextField()
    comment = models.TextField()
    thunder = models.ForeignKey(Thunder, on_delete=models.CASCADE)
    thunder_support_statusCode = models.ForeignKey(ThunderSupport, on_delete=models.SET_NULL, null=True)