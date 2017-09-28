from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Applicant
from .serializers import ApplicantSerializer


@csrf_exempt
def applicant_detail(request, app_id):
    """
    View or update an applicant.
    """
    try:
        applicant = Applicant.objects.get(pk=app_id)
    except Applicant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ApplicantSerializer(applicant)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ApplicantSerializer(job, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create_applicant(request):
    """
    Create an applicant.
    """
    data = JSONParser().parse(request)
    serializer = ApplicantSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
