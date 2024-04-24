from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vinny.views import FraseViewSet

router = routers.DefaultRouter()
router.register('frase', FraseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
