from post.models import *
from rest_framework import serializers
# from users.serializers import AppUserSimpleSerializer, AppUserPhotoOnlySerializer
# from bootstrap.serializers import VideoSerializer, ImageSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['name','size']