from rest_framework import routers
from .api import ChairmanViewSet

router = routers.DefaultRouter()
router.register('api/chairman',ChairmanViewSet,'Add_Chairman')
urlpatterns=router.urls