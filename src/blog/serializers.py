from rest_framework import serializers
from .models import Blog, Category, TableOfContents, KeyTakeaway
from accounts.models import User, Profile


# User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'bios',
                  'facebook_handle', 'twitter_handle', 'linkedin_handle', 'photo']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['email', 'profile']


class TableOfContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOfContents
        fields = ['id', 'title', 'order']


class KeyTakeawaySerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyTakeaway
        fields = ['id', 'content', 'order']



class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    reviewed_by = UserSerializer(read_only=True)
    factchecked_by = UserSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='blog-detail', lookup_field='slug')
    toc_entries = TableOfContentsSerializer(many=True, read_only=True)
    key_takeaways = KeyTakeawaySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['url', 'author', 'reviewed_by', 'factchecked_by', 'title', 'description', 'category', 'slug', 'body',
                  'publish', 'created', 'last_updated', 'image', 'featured', 'status', 'read_time', 'youtube_link', 'download_link', 'download_audio_link', 'toc_entries', 'key_takeaways']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
