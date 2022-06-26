from rest_framework import viewsets

from reviews.models import (
    Category,
    Title,
    Genre,
    Review,
    Comment
)
from .serializers import (
    TitleSerializer,
    ReviewSerializer
)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
