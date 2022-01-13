from firstApp.views import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('firstApp', userviewsets)
