from django.urls import path
from .views import learn, curr_profile

app_name = "profile"

urlpatterns = [
    path('', learn, name="learn-home-page"),
    path('<int:pk>/', curr_profile, name="curr-profile"),
]
