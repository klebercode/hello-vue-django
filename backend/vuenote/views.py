from django.shortcuts import render

from rest_framework import viewsets, permissions

from ..vuenote.models import Note
from ..vuenote.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
