from django.urls import path
from .views import api_example, ApiListUseView 


urlpatterns = [
    path('', ApiListUseView.as_view(), name='users'),
    path('example/', api_example, name='example-api'),
]
