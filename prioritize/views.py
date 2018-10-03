from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

from py2neo import Graph


# Create your views here.
def indexView(request):
	return render(request, 'prioritize/index.html')
def homepage(request):
    return render(request,"prioritize/index.html")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
