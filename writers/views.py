from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Writer
from .serializers import WriterSerializer


class WriterViewSet(ReadOnlyModelViewSet):
    """Эндпоинт для Писателей."""

    queryset = Writer.objects.all().prefetch_related("books")
    serializer_class = WriterSerializer

