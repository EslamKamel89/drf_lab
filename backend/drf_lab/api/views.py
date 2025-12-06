from django.shortcuts import render
from products.models import Product
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        return Response(products)
