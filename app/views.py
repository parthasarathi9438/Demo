from distutils import errors
from distutils.log import error
from email import message
from functools import partial
from os import P_NOWAIT
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import ProductSerializers, ProductModel, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.viewsets import ViewSet



class ProductOperations(APIView):
    def post(self,request):
        #print(request.data)
        ps = ProductSerializers(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {"message":"product saved"}
        else:
            message = {"message":ps.errors}
        return Response(message)

   #get all records
    def get(self, request):
        pm = ProductModel.objects.all()
        ps = ProductSerializers(pm,many=True)
        return Response(ps.data)

class OneProductOperation(APIView):
    def get(self,request,product):
        try:
            res = ProductModel.objects.get(pno=product)
            ps = ProductSerializers(res)
            return Response(ps.data)
        except ProductModel.DoesNotExist:
            message = {"error":"product invalid"}
            return Response(message)

    def put(self,request,product):
        try:
            result = ProductModel.objects.get(pno=product)
            ps = ProductSerializers(result,request.data, partial=True)
            if ps.is_valid():
                ps.save()
                message = {"message":"product updated"}
            else:
                message = {"error":ps.errors}
                return Response(message)
        except ProductModel.DoesNotExist:
            message = {"error":"product invalid"}
            return Response(message)

    def delete(self,request,product):
        delete = ProductModel.objects.filter(pno=product).delete()
        if delete[0] != 0:
            message = {"message":"product deleted"}
        else:
            message = {"message":"invalid product"}
        return Response(message)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class ProductOperationsViewset(ViewSet):
    def list(self, request):
        qs = ProductModel.objects.all()
        ps = ProductSerializers(qs, many=True)
        return Response(ps.data)

    def create(self, request):
        ps = ProductSerializers(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {"success":"product saved"}
        else:
            message = {"error":ps.errors}
        return Response(message)

    


class ProductOperationsOne(ViewSet):
    def retrieve(self,request,pk=None):
        try:
            pm = ProductModel.objects.get(pno=pk)
            #print(pm)
            ps = ProductSerializers(pm)
            return Response(ps.data)
        except ProductModel.DoesNotExist:
            return Response({"error": "Invalid Product"})

    def update(self,request,pk=None):
        try:
            pm = ProductModel.objects.get(pno=pk)
            ps = ProductSerializers(pm,request.data,partial=True)
            if ps.is_valid():
                ps.save()
                message = {"success":"updated"}
            else:
                message = {"error":ps.errors}
                return Response(message)
        except ProductModel.DoesNotExist:
            message = {"error":"invalid product"}
            return Response(message)

    def destroy(self,request,pk=None):
        result = ProductModel.objects.filter(pno=pk).delete()
        if result[0] !=0:
            return Response({"message":"deleted"})
        else:
            return Response({"message":"invalid product"})