from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

# @api_view(['GET'])
# def getUserRoutes(request):
#     routes = [
#         'home_views',
#     ]
#     return Response(routes)


def home_views(request):

 return HttpResponse("this is my jeck")
