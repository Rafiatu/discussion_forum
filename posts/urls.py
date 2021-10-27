from rest_framework.routers import SimpleRouter
from .views import PostView


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


router = OptionalSlashRouter()
router.register(r'', PostView, basename='posts')

urlpatterns = router.urls
