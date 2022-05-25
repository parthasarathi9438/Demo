from pyexpat import model
from attr import fields
from rest_framework import serializers
from app.models import ProductModel
from django.contrib.auth.models import User, Group


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']