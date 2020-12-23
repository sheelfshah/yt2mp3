from django.urls import include, path
from rest_framework import routers
from yt2mp3_app1 import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('music/', views.get_music),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]