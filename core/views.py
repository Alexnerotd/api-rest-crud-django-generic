from .serializers import MyUser, MyUserSerializer
from rest_framework import status, response, views


from django.core.exceptions import BadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
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

class ApiListUseView(views.APIView):

    def get(self, request, format = None):
        users = MyUser.objects.all()
        user_serializer = MyUserSerializer(users, many = True)
        try:
            return response.Response(user_serializer.data, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return response.Response(user_serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, format = None):
        user_serializer = MyUserSerializer(data=self.request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            try:
                return response.Response(user_serializer.data, status=status.HTTP_201_CREATED)
            except BadRequest:
                return response.Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
