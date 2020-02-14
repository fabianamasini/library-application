from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'headoffice', views.HeadOfficeViewSet)
router.register(r'headofficebook', views.HeadOfficeBookViewSet)
router.register(r'collaborator', views.CollaboratorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
