from rest_framework import serializers
from .models import User



class UserRegisterSerializse(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']


    def validate(self, attrs):
        email = attrs.get("email", "")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email", ("email is already been used")}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email",  "avatar", "mobile", "country", "gender" ]