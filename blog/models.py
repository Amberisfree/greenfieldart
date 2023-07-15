

# Create your models here.


# blog/models.py
from django.db import models
from django.urls import reverse # new
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
         on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])



class Review(models.Model): # new
    book = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        if len(self.review) < 15 : return self.review
        return self.review[:11] + ' ...'