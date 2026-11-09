from django.urls import path

from.views import vista_panel_sustetabilidad

urlpatterns = [
    path("panel/", vista_panel_sustetabilidad, name="panel_sustentabilidad")
]