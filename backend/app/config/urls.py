from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health_check(request):
    return JsonResponse({"status": "ok", "service": "Tasque API"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health_check),
]