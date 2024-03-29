
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/user/', views.UserRegisterView.as_view(), name='register_user'),
    path('product/search/<str:name>', views.phone_detail, name='phone_detail'),
    path('category/search/<str:name>', views.category_detail, name='category_detail'),
    path('order/search/<str:name>', views.order_detail, name='order_detail'),
    path('order/list/', views.OrderListView.as_view(), name='order'),
    path('category/list/', views.CategoryListView.as_view(), name='category'),
    path('product/list/', views.ProductListView.as_view(), name='product')
]