# accounts/views.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Serializer to handle the input data for registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Define fields required for registration
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

    def create(self, validated_data):
        # Create the user and hash the password
        user = User.objects.create_user(**validated_data)
        return user

# Register view
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the user to the database
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
