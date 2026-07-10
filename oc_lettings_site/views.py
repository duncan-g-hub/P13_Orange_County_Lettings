"""Views for the project."""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """Display the home page."""
    logger.info("Displaying home page.")
    return render(request, 'index.html')

# TEST ERRORS
#
# def test_404_view(request):
#     return render(request, '404.html')
#
# def test_500_view(request):
#     return render(request, '500.html')
