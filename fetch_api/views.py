# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status

class GetNodesCount(APIView):
    def get(self, request):
        return Response('Temporary Data', status=status.HTTP_200_OK)
