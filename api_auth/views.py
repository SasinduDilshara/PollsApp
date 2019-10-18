from rest_auth.views import LoginView, LogoutView


class LoginViewToken(LoginView):
    authentication_classes = ()


class LogoutViewToken(LogoutView):
    authentication_classes = ()

# Auth key fbbd5735a1d598f841eece3d0b9951260d73f366