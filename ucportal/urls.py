from django.conf.urls import url, include
from rest_framework import routers
from ucportal.ucapi import views
from django.contrib import admin
from rest_framework.authtoken import views as tokenviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'objects', views.ObjectViewSet)
router.register(r'repositories', views.RepositoryViewSet)
router.register(r'ue-sessions', views.UESessionViewSet)
router.register(r'ue-log-credentials', views.UELogCredentialsViewSet, base_name='ue-log-credentials')
router.register(r'ue-frame-scenario', views.UEFrameScenarioViewSet )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls)
]