from .serializers import MyUser, MyUserSerializerGET, MyUserSerializerPOST
from rest_framework import status, response, views, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken


from django.core.exceptions import BadRequest 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
import json

def api_example(request):
    
    example_data_json ={
        "user": [
            "username", "email", "password", "name(not obligatory)", "last_name(not obligatory)",
        ]
    }
    example_serializer = json.dumps(example_data_json)

    return JsonResponse(example_serializer, safe=False)


# Create your views here.
class UsersApiList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializerPOST


class UserApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()

    serializer_class = MyUserSerializerPOST
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
    
        
