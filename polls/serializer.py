from rest_framework import serializers
from polls.models import *
# from users.serializers import AppUserSimpleSerializer, AppUserPhotoOnlySerializer
# from bootstrap.serializers import VideoSerializer, ImageSerializer


class QuestionSerializer(serializers.ModelSerializer):
    # user = AppUserSimpleSerializer(read_only=True)
    # liked_users = AppUserPhotoOnlySerializer('liked_users', many=True)
    # tags = serializers.StringRelatedField(many=True)
    isRecent = serializers.SerializerMethodField('was_published_recently')
    # video_data = serializers.SerializerMethodField('get_video')

    def was_published_recently(self,obj):
        return obj.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def get_image(self, obj):
    #     if obj.post_type == PostType.IMAGE.value:
    #         return ImagePostPartialSerializer().to_representation(obj.get_image())

    # def get_video(self, obj):
    #     if obj.post_type == PostType.VIDEO.value:
    #         return VideoPostPartialSerializer().to_representation(obj.get_video())

    class Meta:
        model = Question
        fields = ['question_text','pub_date','isRecent' ]


class ChoiceSerializer(serializers.ModelSerializer):
    # user = AppUserSimpleSerializer('user')
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    # reply_comments = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=True)

    class Meta:
        model = Choice
        fields = ['question','choice_text','votes']


# # Simple Serializers
# ##########################################################

# class PostSimpleSerializer(serializers.ModelSerializer):
#     user = AppUserSimpleSerializer(read_only=True)
#     data = serializers.SerializerMethodField('get_data')
#     tags = serializers.StringRelatedField(many=True)

#     def get_data(self, obj):
#         if obj.post_type == PostType.IMAGE.value:
#             image_post = obj.get_image()
#             return {
#                 'content': image_post.content,
#                 'image': image_post.image.content
#             }
#         elif obj.post_type == PostType.VIDEO.value:
#             video_post = obj.get_video()
#             return {
#                 'thumbnail': video_post.video.thumbnail.content,
#                 'video': video_post.video.content
#             }

#     class Meta:
#         model = Post
#         fields = ['entity_id', 'post_type', 'title', 'timestamp', 'user',
#                   'number_of_likes', 'number_of_comments', 'data', 'tags']


# class ImagePostSimpleSerializer(serializers.ModelSerializer):
#     user = AppUserSimpleSerializer(read_only=True)
#     image = serializers.ReadOnlyField(source='image.content')

#     class Meta:
#         model = ImagePost
#         fields = ['entity_id', 'title', 'content', 'timestamp', 'user',
#                   'number_of_likes', 'number_of_comments', 'image']


# class VideoPostSimpleSerializer(serializers.ModelSerializer):
#     user = AppUserSimpleSerializer(read_only=True)
#     video = serializers.ReadOnlyField(source='video.content')
#     thumbnail = serializers.ReadOnlyField(source='video.thumbnail.content')

#     class Meta:
#         model = VideoPost
#         fields = ['entity_id', 'title', 'timestamp', 'user',
#                   'number_of_likes', 'number_of_comments', 'video', 'thumbnail']


# class PostCommentSimpleSerializer(serializers.ModelSerializer):
#     user = AppUserSimpleSerializer('user')

#     class Meta:
#         model = PostComment
#         fields = ['id', 'user', 'timestamp', 'content', 'number_of_likes',
#                   'number_of_reply_comments']


# # Partial Serializers
# ##########################################################

# class VideoPostPartialSerializer(serializers.ModelSerializer):
#     video = VideoSerializer('video')

#     class Meta:
#         model = VideoPost
#         fields = ['video']


# class ImagePostPartialSerializer(serializers.ModelSerializer):
#     image = ImageSerializer('image')

#     class Meta:
#         model = ImagePost
#         fields = ['content', 'image']


# class PostTopCommentsSerializer(serializers.ModelSerializer):
#     top_comments = PostCommentSimpleSerializer('top_comments', many=True)

#     class Meta:
#         model = Post
#         fields = ['top_comments']


# class CommentRepliesSerializer(serializers.ModelSerializer):
#     comment = serializers.SerializerMethodField('get_current_object')
#     reply_comments = PostCommentSimpleSerializer('reply_comments', many=True)

#     def get_current_object(self, obj):
#         return PostCommentSerializer().to_representation(obj)

#     class Meta:
#         model = PostComment
#         fields = ['comment', 'reply_comments']
