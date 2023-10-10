from django.urls import path

from network.views import NetworkNodeListAPI, NetworkNodeCreateAPI, NetworkNodeDetailAPI, NetworkNodeUpdateAPI, \
    NetworkNodeDeleteAPI, ProductListAPI, ProductCreateAPI, ProductDetailAPI, ProductUpdateAPI, ProductDeleteAPI, \
    ContactListAPI, ContactCreateAPI, ContactDetailAPI, ContactUpdateAPI, ContactDeleteAPI

app_name = 'network'

urlpatterns = [
    path('networknode/', NetworkNodeListAPI.as_view(), name='networknode_list'),
    path('networknode/create/', NetworkNodeCreateAPI.as_view(), name='networknode_create'),
    path('networknode/detail/<int:pk>/', NetworkNodeDetailAPI.as_view(), name='networknode_detail'),
    path('networknode/delete/<int:pk>/', NetworkNodeDeleteAPI.as_view(), name='networknode_delete'),
    path('networknode/update/<int:pk>/', NetworkNodeUpdateAPI.as_view(), name='networknode_update'),
    path('product/', ProductListAPI.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPI.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
    path('product/delete/<int:pk>/', ProductDeleteAPI.as_view(), name='product_delete'),
    path('product/update/<int:pk>/', ProductUpdateAPI.as_view(), name='product_update'),
    path('contact/', ContactListAPI.as_view(), name='contact_list'),
    path('contact/create/', ContactCreateAPI.as_view(), name='contact_create'),
    path('contact/detail/<int:pk>/', ContactDetailAPI.as_view(), name='contact_detail'),
    path('contact/delete/<int:pk>/', ContactDeleteAPI.as_view(), name='contact-delete'),
    path('contact/update/<int:pk>/', ContactUpdateAPI.as_view(), name='contact-update'),
]
