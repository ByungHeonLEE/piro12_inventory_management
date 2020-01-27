from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.views import list_product, detail_product, reg_product, reg_client, detail_client, list_client, update_client, \
    update_product, delete_client, delete_product, minus_product, plus_product

urlpatterns = [
    path('', list_product, name='list_product'),
    path('product/detail/<int:pk>/', detail_product, name='detail_product'),
    path('product/registration/', reg_product, name='reg_product'),
    path('client/registration/', reg_client, name='reg_client'),
    path('client/detail/<int:pk>/', detail_client, name='detail_client'),
    path('client/list/', list_client, name='list_client'),
    path('client/update/<int:pk>/', update_client, name='update_client'),
    path('product/update/<int:pk>/', update_product, name='update_product'),
    path('client/delete/<int:pk>/', delete_client, name='delete_client'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product'),
    path('product/minus/<int:pk>/', minus_product, name='minus_product'),
    path('product/plus/<int:pk>/', plus_product, name='plus_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
