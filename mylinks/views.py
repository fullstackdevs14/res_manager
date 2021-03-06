from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .es_client import es_client
from .search import MyLinkIndex
from .models import MyLink
from .serializers import MyLinkSerializer

class MyLinkViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MyLink.objects.all()
    serializer_class = MyLinkSerializer

class FilterView(es_views.ListElasticAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    es_client = es_client
    es_model = MyLinkIndex
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter,
    )
    es_filter_fields = (
        es_filters.ESFieldFilter('tag', 'tags'),
    )
    es_search_fields = (
        'tags',
        'desc',
        'owner',
        'source'
    )