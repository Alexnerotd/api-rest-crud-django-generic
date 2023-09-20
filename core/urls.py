from django.urls import path
from .views import api_example, ApiListUseView 


urlpatterns = [
    path('example/', api_example, name='example-api'),
    path('', ApiListUseView.as_view(), name='users')
]
