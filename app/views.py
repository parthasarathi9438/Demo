from email import message
from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import ProductSerializers, ProductModel



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