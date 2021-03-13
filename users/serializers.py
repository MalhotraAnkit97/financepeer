from rest_framework.serializers import Serializer,ModelSerializer, FileField, ListField
from .models import user
# Serializers define the API representation.

class UserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['userid', 'id', 'title']

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        model = user
        fields = ['file']


# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(Serializer):
    file_uploaded = ListField(FileField())
    class Meta:
        fields = ['file_uploaded']