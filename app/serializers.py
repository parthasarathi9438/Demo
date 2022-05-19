from pyexpat import model
from attr import fields
from rest_framework import serializers
from app.models import ProductModel


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"