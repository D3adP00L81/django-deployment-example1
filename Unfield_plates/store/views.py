from django.shortcuts import render
from .models import Order,OrderItem,ShippingAddress,Product
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

class StoreCategoryView(TemplateView):
    template_name = 'store_category.html'
    context_object_name = 'store:category-page'

class StoreProductListView(ListView):
    model = Product
    template_name = 'store_products_lists.html'
    paginate = 200

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class StoreProductDetailView(DetailView):
    model = Product
    template_name = 'store_products_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ShoppingCardListView(ListView):
    model = OrderItem
    template_name = 'store_shopping_card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#######################################
#######################################
