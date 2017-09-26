from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from job.serializers import JobViewSet, JobSerializer
from experience.serializers import ExperienceViewSet
from applicant.serializers import ApplicantViewSet


router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
