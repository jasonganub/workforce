from rest_framework import routers, serializers, viewsets
from .models import Experience


# Serializers define the API representation.
class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ('applicant', 'category', 'start', 'end', 'description', 'institution')

# ViewSets define the view behavior.
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
