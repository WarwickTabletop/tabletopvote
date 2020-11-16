from django.contrib import admin
from django.urls import path, include

from .views import VoteView, DoneView

app_name = "vote"

urlpatterns = [
    path('<int:id>/', VoteView.as_view(), name="vote"),
    path('<int:election>/<uuid:slug>', DoneView.as_view(), name="vote_done")
]