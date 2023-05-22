"""Views for the user API."""

from rest_framework import generics, authentication, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import viewsets
from rest_framework.decorators import action


from core.models import User
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,

)
from core.models import User


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    # def post(self, *args, **kwargs):
    #     """
    #         Create a MyModel
    #         ---
    #         parameters:
    #             - name: source
    #               description: file
    #               required: True
    #               type: file
    #         responseMessages:
    #             - code: 201
    #               message: Created
    #     """
    #     return super(CreateUserView, self).post(self, *args, **kwargs)


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.order_by('-created_at')
#     serializer_class = UserSerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)
