from django.urls import path

from . import views

urlpatterns = [
    path('catalogs', views.catalogs, name='catalogs'),
    path(r'catalogs/<int:year>/<int:month>/<int:day>', views.catalogs_date, name='date'),
    path(r'elements/<slug:fullname>', views.get_elements),
    path(r'elements/<slug:fullname>/<slug:version>', views.get_elements)
]
