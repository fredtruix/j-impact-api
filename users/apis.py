from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserRegisterSerializse, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



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
    # lookup_field = "email"


    def get_object(self):
        return self.request.user