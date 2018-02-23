from django.shortcuts import render
from rest_framework import viewsets, status, renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import MyLink, Owner, Tag
from .serializers import MyLinkSerializer, OwnerSerializer, TagSerializer

class MyLinkViewSet(viewsets.ModelViewSet):
    queryset = MyLink.objects.all()
    serializer_class = MyLinkSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@api_view(['GET'])
def mylinks_root(request, format=None):
    return Response({
        'mylinks': reverse('mylink-list', request=request, format=format),
        'owners': reverse('owner-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format),
    })

@api_view(['POST'])
def filterLinks(request, format=None):
    return Response(request.data)