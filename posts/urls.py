from rest_framework.routers import SimpleRouter
from .views import PostView


router = SimpleRouter(trailing_slash=False)
router.register(r'', PostView, basename='posts')

urlpatterns = router.urls
