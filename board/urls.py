from rest_framework.routers import DefaultRouter

from views import SprintViewSet, TaskViewSet, UserViewSet


router = DefaultRouter()
router.register(r'sprints', SprintViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)