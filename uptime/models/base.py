from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='+', on_delete=models.CASCADE)


    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PeopleManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(created_by=user)