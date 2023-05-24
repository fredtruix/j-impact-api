from rest_framework import serializers
from .models import Blog, Group



class BlogsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Blog
        fields = ["id", "user","title","content","images","updated","created","views","likes"]


class GroupSerializer(serializers.ModelSerializer):


    class Meta:
        model = Group
        fields = ["id", "host", "topic", "name", 'description', "participants", "updated", "created"]