from rest_framework import routers, serializers, viewsets
from .models import Applicant


# Serializers define the API representation.
class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicant
        fields = ('applicant', 'category', 'start', 'end', 'description', 'institution')

# ViewSets define the view behavior.
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
