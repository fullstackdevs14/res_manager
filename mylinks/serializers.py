from rest_framework import serializers
from .models import MyLink, Owner, Tag

class MyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLink
        fields = ('id', 'url', 'tags', 'desc', 'source', 'owner')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'