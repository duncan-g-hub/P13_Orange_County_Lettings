from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls"), name='lettings_index'),
    path('profiles/', include("profiles.urls"), name='profiles_index'),
    path('admin/', admin.site.urls),
]
