from django.urls import path, re_path

from . import views

app_name = "profiles"

urlpatterns = [
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<slug:id>/update/",
         views.ProfileUpdateView.as_view(), name="update"),
]
