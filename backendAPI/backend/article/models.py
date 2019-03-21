from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .validators import StepValueValidator

class Article(models.Model):
    PUBLISHED = 1
    PRIVATE = 2
  
    STATUS_CHOICES = (
        (PUBLISHED, "Published"),
        (PRIVATE, "PRIVATE"),
    )
    
    """ Article """
    owner = models.ForeignKey('tbpauth.User',
                               on_delete=models.CASCADE,
                               related_name='article_owner')

    title = models.CharField("タイトル", max_length=128)

    body = models.TextField(
        verbose_name='ボディー',
        blank=False,
        null=True,
        max_length=50000,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title