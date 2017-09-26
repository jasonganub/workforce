from rest_framework import routers, serializers, viewsets
from job.models import Job


# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields= ('title', 'location', 'description')

# ViewSets define the view behavior.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
