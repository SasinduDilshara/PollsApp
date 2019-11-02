from django.urls import path

from . import views

urlpatterns = [
path('', views.Details.as_view()),
    path('<username>/', views.UserDetail.as_view()),
    # path('choice', views.ChoiceList.as_view()),
]
# path(route, view, kwargs=None, name=None)