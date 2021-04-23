from django.contrib.auth.models import User, Group
from ucportal.ucapi.models import Model, UESession, Object, Repository, UEFrameScenario
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from ucportal.ucapi.serializers import UserSerializer, GroupSerializer, ModelSerializer, UESessionSerializer, ObjectSerializer, RepositorySerializer, UEFrameScenarioSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class ModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UC App 3D model information to be viewed or edited
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    
    
class UESessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UC App session information to be posted
    """
    queryset = UESession.objects.all()
    serializer_class = UESessionSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, activation_code="asdf1234")
    
class UELogCredentialsViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieve Amazon S3 log uploading information and credentials
    """
    def list(self, request, format=None):
        latest_publish = "some_credentials"
        
        return Response({
            "type": "s3",
            "data": { "AccessKeyId" : "AccessKeyId",
                      "SecretAccessKey" : "SecretAccessKey",
                      "SessionToken" : "SessionToken",
                      "Expiration" : "Expiration",
                      "Bucket" : "Bucket",
                      "Key" : "Key",
                      "Region" : "Region" }
        })

        
class ObjectViewSet(ModelViewSet):
    """
    API endpoint that allows UC App 3D model information to be viewed or edited
    """
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))
                       
class RepositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UC App repositories to be viewed or edited
    """
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    

class UEFrameScenarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UC App 3D model information to be viewed or edited
    """
    queryset = UEFrameScenario.objects.all()
    serializer_class = UEFrameScenarioSerializer

    