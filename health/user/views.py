"""Views for the user API."""

from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,

)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # type: ignore
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'token': token.key,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'first_time_login': user.first_time_login,
            'image': user.image.path,
        }
        if user.first_time_login:
            user.first_time_login = False
            user.save(update_fields=['first_time_login'])
            response_data['first_time_login'] = True

        return Response(response_data, status=status.HTTP_200_OK)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
