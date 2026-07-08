"""Project URL configuration."""

from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),




    # TEST ERRORS
    # path('404/', views.test_404_view),
    # path('500/', views.test_500_view)
]
