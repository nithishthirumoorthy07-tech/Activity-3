from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AttendanceViewSet, StudentViewSet, dashboard_stats

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('dashboard/', dashboard_stats, name='dashboard-stats'),
    path('', include(router.urls)),
]
