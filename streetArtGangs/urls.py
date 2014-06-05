from django.conf.urls import patterns, url, include
from server import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

admin.autodiscover()

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'venues', views.VenueViewSet)
router.register(r'gangsters', views.UserProfileViewSet)
router.register(r'gangs', views.GangViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)
#router.register(r'policeBust', views.PoliceBustViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^authentication/', views.UserAuthView.as_view(),
        name='user-detail'),
    url(r'^police/(\d)/$', 'server.views.policeBust'),
    url(r'^events/(\d)/playername/(\w+)/playerpos/(.+)/playerinfo/(.+)/playerdata/(.+)/$', 'server.views.eventHappened'),
    url(r'^heatmaps/eventid/(.+)/time/(.+)/$', 'server.views.getHeatMapData'),    
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
