from django.urls import path
from .views import api_example, UsersApiList, UserApiDetail 

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/example/', api_example, name='example-api'),
    path('api/users/', UsersApiList.as_view(), name='users'),
    path('api/users/<int:pk>/', UserApiDetail.as_view(), name="user"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
