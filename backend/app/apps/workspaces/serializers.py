from rest_framework import serializers

from .models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Workspace
        fields = ["id", "owner", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]