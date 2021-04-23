from rest_framework import viewsets
from rest_framework.response import Response
from .models import Club
from .serializers import ClubSerializer
from .serializers import ClubFullSerializer


# create ViewSet for clubs
class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

    # change serializer to get more info about club after choose particular id
    def retrieve(self, request, *args, **kwargs):
        club = self.get_object()
        serializer = ClubFullSerializer(club)
        return Response(serializer.data)
