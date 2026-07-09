from django.urls import reverse, resolve

from oc_lettings_site.views import index

def test_url_index():
    url = reverse('index')
    assert resolve(url).view_name == 'index'
    assert resolve(url).func == index