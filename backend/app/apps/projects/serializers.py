from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    workspace_name = serializers.CharField(source="workspace.name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "workspace",
            "workspace_name",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "workspace_name", "created_at", "updated_at"]