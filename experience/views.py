from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Experience
from .serializers import ExperienceSerializer


@csrf_exempt
def create_experience(request):
    """
    Create an experience.
    """
    data = JSONParser().parse(request)
    serializer = ExperienceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
