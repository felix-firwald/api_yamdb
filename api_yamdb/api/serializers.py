from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Title, Review


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    title_id = SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        fields = '__all__'
        model = Review
