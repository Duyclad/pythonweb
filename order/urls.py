from django.urls import path
from  .views import order_create


urlpatterns = [
    path('',order_create().as_view(),name='order' ),
]

