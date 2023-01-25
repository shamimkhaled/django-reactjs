from django.views import generic
from django.shortcuts import render, redirect
from product.models import Variant
from product.models import Product
from product.models import ProductVariant


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductListView(generic.TemplateView):
     # model = Product
     template_name = 'products/list.html'
     # context_object_name = 'product'
     # paginate_by=2
     def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = Product.objects.filter().values('id', 'title')
        #context['product'] = True
        context['products'] = list(products.all())
        return context





#Make a List View of Product Table
class ListViewProductTable(generic.TemplateView):  
      #model = ProductVariant      
     template_name = 'products/item-list.html'
      #context_object_name = 'products'
     def get_context_data(self, **kwargs):
        context = super(ListViewProductTable, self).get_context_data(**kwargs)
        variants = ProductVariant.objects.filter().values('variant_id', 'variant_title')
        #context['products'] = True
        context['variants'] = list(variants.all())
        return context

# Create Product Views from newly created url 
class CreateViewProduct(generic.TemplateView):
    template_name = 'products/create-product.html'

    def get_context_data(self, **kwargs):
        context = super(CreateViewProduct, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context






    
        