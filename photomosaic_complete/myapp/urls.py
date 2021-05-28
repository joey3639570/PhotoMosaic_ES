from django.urls import path
from django.conf.urls import url
from .views import my_view, mosaicing, mosaicing_view

urlpatterns = [
    path('', my_view, name='my-view'),
    path('mosaic_act/', mosaicing_view, name='mosaic_act'),
    url(r'^mosaic', mosaicing, name='mosaic')
]
