from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='combo:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url','id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
        extra_kwargs = { 'url' : { 'view_name':'combo:snippet-detail' }, }
        


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='combo:snippet-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
        extra_kwargs = { 'url' : { 'view_name':'combo:user-detail' }, }


#классы от Quickstart
class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

