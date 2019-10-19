from users.models import AppUser
from users.serializer import *
from rest_framework import generics
from rest_framework import permissions



class Details(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]
