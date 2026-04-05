from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RecordViewSet, dashboard

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard),
]