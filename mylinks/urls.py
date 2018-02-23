from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MyLinkViewSet, OwnerViewSet, TagViewSet, mylinks_root, filterLinks

list = {
    'get': 'list',
    'post': 'create'
}
detail = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = format_suffix_patterns([
    url(r'^$', mylinks_root, name="mylinks-root"),
    url(r'^mylinks$', MyLinkViewSet.as_view(list), name='mylink-list'),
    url(r'^mylinks/(?P<pk>[0-9]+)$', MyLinkViewSet.as_view(detail), name='mylink-detail'),
    url(r'^owners$', OwnerViewSet.as_view(list), name='owner-list'),
    url(r'^owners/(?P<pk>[0-9]+)$', OwnerViewSet.as_view(detail), name='owner-detail'),
    url(r'^tags$', TagViewSet.as_view(list), name='tag-list'),
    url(r'^tags/(?P<pk>[0-9]+)$', TagViewSet.as_view(detail), name='tag-detail'),
    url(r'^filter$', filterLinks, name="mylinks-filter")
])