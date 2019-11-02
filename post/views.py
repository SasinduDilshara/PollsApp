from post.models import *
from post.serializer import *
from rest_framework import generics
from rest_framework import permissions

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
