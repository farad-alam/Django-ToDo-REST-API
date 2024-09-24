from django.shortcuts import render, HttpResponse

from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer, UserListSerializer

# class UserCreateView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer


# class UserListView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserListSerializer

class UserCreateListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# class UserDetailedUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     lookup_field = 'id'


class UserDetailedUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'


def registration_view(request):
    return HttpResponse('sound from accounts!!!')