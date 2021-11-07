from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import StoreCategoryView,StoreProductListView,StoreProductDetailView,ShoppingCardListView

app_name = 'store'

urlpatterns = [
        path('store/category/',StoreCategoryView.as_view(),name='category-page'),
        path('store/list/', StoreProductListView.as_view(), name='product-list'),
        path('store/detail/<int:pk>',StoreProductDetailView.as_view(),name='product-exact-detail'),
        path('store/<int:pk>/shoppingcard',ShoppingCardListView.as_view(),name='shopping-card'),
]
