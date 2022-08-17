from posixpath import basename
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import carreraView

router = DefaultRouter()
router.register(r'carreras', carreraView, basename="carreras")

urlpatterns = [
    path('',include(router.urls))
]