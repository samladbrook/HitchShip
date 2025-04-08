from django.contrib import admin
from django.urls import path, include  # Include function to include other URLconf modules
from rest_framework_simplejwt import views as jwt_views  # JWT token views for authentication

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin site
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain endpoint
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh endpoint

    # Include the URLs from the 'accounts' app for register and login
    path('accounts/', include('hitchship_backend.accounts.urls')),  # This links to the 'accounts' app URLs
]
