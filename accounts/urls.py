from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import ProfileUpdateView
from accounts.views import profileDetailView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register/",StudentCreateView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    path("jwt/token/",TokenObtainPairView.as_view()),

    path("jwt/token/refresh/",TokenRefreshView.as_view()),

    path("profile/complete/",ProfileUpdateView.as_view()),
    path("profile/me/",profileDetailView.as_view()),
]