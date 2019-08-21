from django.urls import path, include

from rest_framework import routers

from ..vuenote import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
