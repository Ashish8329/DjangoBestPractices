from django.shortcuts import render

# Two main ways of view fbv and cbv

# fbv
from django.http  import JsonResponse
from urllib import request
def hell_world(request):
    return JsonResponse({'message':"hello world"})


# cbv
from django.views import View

class HelloWorldView(View):
    def get(self, request):
        return JsonResponse({'message': 'Hello, Django!'})
    # Django's views handle standard HTTP requests (GET, POST, PUT, DELETE) for web applications (HTML pages, forms, etc.).



# Django REST Framework extends Django’s view system to handle RESTful APIs by introducing APIView and ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldAPI(APIView):
    def get(self, request):
        return Response({'message': 'Hello, DRF!'})
    


# also provide a fbv with apiview
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello_world_apiview(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})




# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().

# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response

# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)