from rest_framework import serializers
from .models import Club


# base info about club before choose particular club id
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'crest']


# detailed info after choose particular club id
class ClubFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'nickname', 'description', 'found_date',
                  'stadium', 'stadium_capacity', 'number_of_titles', 'crest']
