from django.urls import include
from django.urls import path
from api_auth.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
   path('', include('rest_auth.urls')),
]

urlpatterns = [
    path('login/',
         csrf_exempt(LoginViewToken.as_view()), name='rest_login'),
    path('logout/',
         csrf_exempt(LogoutViewToken.as_view()), name='rest_logout'),
    path('', include('rest_auth.urls')),
]