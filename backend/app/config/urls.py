from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def health_check(request):
    return JsonResponse({"status": "ok", "service": "Tasque API"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health_check),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]