from django.urls import path
from  .views import LoginClass
from .views import register
from .views import forgotpass


urlpatterns = [
    path('',LoginClass.as_view(),name='login' ),
    #path('',register.as_view(),name='register' ),
    #path('', forgotpass.as_view(), name='forgotpass'),

]


