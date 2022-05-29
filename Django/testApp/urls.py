from django.urls import path
from .views import delete_profile, learn, curr_profile, delete_profile, create_profile, update_profile

app_name = "profile"

urlpatterns = [
    path('', learn, name="learn-home-page"),
    path('<int:pk>/', curr_profile, name="curr-profile"),
    path('<int:pk>/delete', delete_profile, name="delete-profile"),
    path('create', create_profile, name="create-profile"),
    path("<int:pk>/update", update_profile, name="update-profile")
]
