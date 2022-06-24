from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        max_length=100
    )


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    category = models.ForeignKey(
        Category,
        related_name='titles'
    )


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        max_length=100
    )


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)]
    )
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    review_id = ''
    text = ''
    author = ''
    pub_date = ''
