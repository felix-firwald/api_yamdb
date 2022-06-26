from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'USR'
    MODERATOR = 'MOD'
    ADMIN = 'ADM'
    CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    ]
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=3,
        choices=CHOICES,
        default=USER
    )


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
        related_name='titles',
        on_delete=models.CASCADE
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
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
