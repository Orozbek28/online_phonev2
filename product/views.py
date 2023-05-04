from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import pagination
from rest_framework import generics, mixins
from rest_framework.decorators import api_view

from .models import Category, Product, Order, User
from .permissions import IsAuthenticatedOrSafeMethods
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, UserRegisterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]




@api_view(['GET'])
def category_detail(request, name):
    product = Category.objects.get(name=name)
    serializer = CategorySerializer(product)
    return Response(serializer.data)


class TweetPagination(pagination.PageNumberPagination):
    page_size = 2


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['created', ]
    pagination_class = TweetPagination


@api_view(['GET'])
def phone_detail(request, name):
    product = Product.objects.get(name=name)
    serializer = ProductSerializer(product)
    if serializer:
        return Response(serializer.data)
    return Response(serializer.errors, status=400)





class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods]


@api_view(['GET'])
def order_detail(request, name):
    product = Order.objects.get(name=name)
    serializer = OrderSerializer(product)
    if serializer:
        return Response(serializer.data)
    return Response(serializer.errors, status=400)




 
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# class OrderListView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
#
# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
#
#
# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer















