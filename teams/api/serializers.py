from rest_framework.serializers import ModelSerializer
from teams.model import Team

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = 
