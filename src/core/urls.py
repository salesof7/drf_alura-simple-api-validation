from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients import views as clients_view

router = routers.DefaultRouter()
router.register('clients', clients_view.ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
