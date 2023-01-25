from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductListView, ListViewProductTable, CreateViewProduct
from product.views.variant import VariantView, VariantCreateView, VariantEditView
from django.conf.urls.static import static
from config import settings

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),

    # listview of product table url
    path('item-list/', ListViewProductTable.as_view(), name='item-list.product'),
    path('create-product/', CreateViewProduct.as_view(), name='create-product.product'),
] 
#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
