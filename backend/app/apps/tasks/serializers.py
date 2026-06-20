from rest_framework import serializers

from apps.projects.models import Project
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    assignee_email = serializers.EmailField(source="assignee.email", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "project_name",
            "assignee",
            "assignee_email",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "project_name", "assignee_email", "created_at", "updated_at"]

    def validate_project(self, project):
        request = self.context.get("request")

        if project.workspace.owner != request.user:
            raise serializers.ValidationError("You can only create tasks in your own projects.")

        return project

    def validate_assignee(self, assignee):
        request = self.context.get("request")

        if assignee and assignee != request.user:
            raise serializers.ValidationError("For now, you can only assign tasks to yourself.")

        return assignee