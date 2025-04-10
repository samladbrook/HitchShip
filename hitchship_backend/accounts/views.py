# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

# Custom user serializer
from .serializers import UserSerializer, LoginSerializer

# Register View
@api_view(['POST'])
def register(request):
    """
    Register a new user and return a JWT token.
    """
    if request.method == 'POST':
        # Extract the user data from the request
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate the token after registration
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Return the JWT token
            return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
@api_view(['POST'])
def login(request):
    """
    Login and return JWT token if credentials are correct.
    """
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate the input
        if not email or not password:
            return Response({"error": "Email and password are required!"}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Generate JWT token for authenticated user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access': access_token, 'refresh': str(refresh)}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)

