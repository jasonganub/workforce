from django.conf.urls import include, url
from django.contrib import admin
from job import urls
from applicant import urls


urlpatterns = [
    url(r'^jobs/', include('job.urls')),
    url(r'^applicants/', include('applicant.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
