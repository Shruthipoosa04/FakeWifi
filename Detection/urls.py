from django.urls import path
from .views import wifi_list

urlpatterns = [
    path('api/wifi/', wifi_list, name='wifi-list'),
]

from .views import index

urlpatterns = [
    path('', index, name='home'),
]

from .views import check_new_fake_networks

urlpatterns += [
    path('api/check_fake/', check_new_fake_networks, name='check_fake'),
]
