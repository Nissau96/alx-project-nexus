from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Online Poll System API",
      default_version='v1',
      description="API documentation for the Project Nexus Online Polls Solution",
      contact=openapi.Contact(email="uxperiencelabs@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


swagger_ui_settings = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT authorization header. Example: "Bearer {token}"'
        }
    }
}




urlpatterns = [
    path('', RedirectView.as_view(url='api/docs/', permanent=True)),
    path('admin/', admin.site.urls),

    # API Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # Poll App Endpoints
    path('api/', include('polls.urls')),

    # API Documentation Endpoints
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]