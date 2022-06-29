from rest_framework import routers
from .views import WriterViewSet


router = routers.DefaultRouter()

router.register("writers", WriterViewSet, basename="writers")

urlpatterns = router.urls
