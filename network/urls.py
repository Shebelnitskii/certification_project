from django.urls import path

from network.views import NetworkNodeListAPI, NetworkNodeCreateAPI, NetworkNodeDetailAPI, NetworkNodeUpdateAPI, \
    NetworkNodeDeleteAPI

app_name = 'network'

urlpatterns = [
    path('networknode/', NetworkNodeListAPI.as_view(), name='networknode-list'),
    path('networknode/create/', NetworkNodeCreateAPI.as_view(), name='networknode-create'),
    path('networknode/detail/<int:pk>/', NetworkNodeDetailAPI.as_view(), name='networknode-detail'),
    path('networknode/delete/<int:pk>/', NetworkNodeUpdateAPI.as_view(), name='networknode-delete'),
    path('networknode/update/<int:pk>/', NetworkNodeDeleteAPI.as_view(), name='networknode-update'),
]