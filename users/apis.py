from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserRegisterSerializse, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Jwt to get all user details along with tokens
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializse

    def post(self, request):
        serializer = UserRegisterSerializse(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class ProfileDetailsView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get_object(self):
        return self.request.user