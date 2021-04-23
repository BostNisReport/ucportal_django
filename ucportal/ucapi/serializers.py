from django.contrib.auth.models import User, Group
from ucportal.ucapi.models import Model, UESession, Object, Repository, UEFrameScenario
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ('url','created', 'name', 'description', 's3bucket', 's3region', 's3key')
        
class UESessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UESession
        fields = ('url','created', 'machine_id', 'activation_code', 'log_name', 'version', 'owner')
        read_only_fields = ('created', 'activation_code', 'owner')
        
class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ('url','created', 'name', 'owner')
        read_only_fields = ('created', 'owner')
        
class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repository
        fields = ('url','name', 'remote_url', 'users')
        
class UEFrameScenarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UEFrameScenario
        fields = ('url','name', 'description', 'model', 'groups', 'users')
        read_only_fields = ('groups', 'users')