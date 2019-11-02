from users.models import AppUser
from users.serializer import *
from rest_framework import generics
from rest_framework import permissions



class Details(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class UserDetail(generics.RetrieveAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    # User user argument 'username' to look up auth->username
    lookup_field = 'auth__username'
    lookup_url_kwarg = 'username'

    permission_classes = [permissions.IsAuthenticated]
