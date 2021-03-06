from rest_framework.viewsets import ModelViewSet
from teams.models import Team
from .serializers import TeamSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.all()
    serializer_class = TeamSerializer
