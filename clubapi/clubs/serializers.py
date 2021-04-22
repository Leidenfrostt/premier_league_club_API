from rest_framework import serializers
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'crest']


class ClubFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'nickname', 'description', 'found_date',
                  'stadium', 'stadium_capacity', 'number_of_titles', 'crest']
