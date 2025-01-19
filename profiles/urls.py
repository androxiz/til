from django.urls import path

from . import views


from django.conf import settings
from django.conf.urls.static import static
app_name = 'profiles'

urlpatterns = [
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
    path("<str:username>/settings/", views.SettingsView.as_view(), name="settings"),
]