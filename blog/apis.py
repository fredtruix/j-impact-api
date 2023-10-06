from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from .serializers import BlogsSerializer, GroupSerializer, TopicSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Blog, Group, Topic
from rest_framework.response import Response
from users.models import User
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication




class BlogListView(ListCreateAPIView):
    serializer_class = BlogsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Blog.objects.all()


@api_view(["GET"])
@permission_classes((IsAuthenticated))
def UserBlogList(request, id):
    try:
        user = User.objects.get(id=id)
        blog = Blog.objects.filter(user=user.id)
        serializer = BlogsSerializer(blog,  many=True)
    except :
        return Response({})
    return Response(serializer.data)
    



@api_view(["GET", "PATCH", "DELETE"])
@permission_classes((IsAuthenticated))
def blog_update_delete(request, user_id, blog_id):
    try:
        user = User.objects.get(id=user_id)
        blog = Blog.objects.get(user=user, id=blog_id)

        if request.method == "PATCH":
            serializer = BlogsSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "GET":
            serializer = BlogsSerializer(blog)
            return Response(serializer.data)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    except Blog.DoesNotExist:
        return Response({"error": "Blog not found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated))
def Group_list_create(request):
    group = Group.objects.all()
    if request.method == "POST":
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)
    
    return Response({})


@api_view(["GET","PATCH","DELETE"])
@permission_classes((IsAuthenticated))
def read_update_delete_group(request, user_id, group_id):
    try:
        user = User.objects.get(id=user_id)
        group = Group.objects.get(host=user.id, id = group_id)
        if request.POST == "PATCH":
            serializer = GroupSerializer(group, data=request.data)
            if serializer.is_valid():
                serializer.save()
        elif request.method == "DELETE":
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = GroupSerializer(group, many=False)
            return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    except Group.DoesNotExist:
        return Response({"error": "Group not found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((IsAuthenticated))
def Read_topics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
