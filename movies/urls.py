from django.urls import URLPattern, path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'casts',views.CastViewSet)
router.register(r'directors',views.DirectorViewSet)
router.register(r'genres',views.GenreViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]