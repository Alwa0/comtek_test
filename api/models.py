from django.core.validators import validate_slug
from django.db import models


class Catalog(models.Model):
    class Meta:
        unique_together = (('fullname', 'version'),)
    id = models
    fullname = models.CharField(max_length=200, validators=[validate_slug])
    shortname = models.CharField(max_length=100, validators=[validate_slug])
    description = models.CharField(max_length=400)
    version = models.CharField(max_length=10, blank=False)
    start_date = models.DateField("Version start day")

    def __str__(self):
        return f"{self.fullname}.{self.version}"


class Element(models.Model):
    catalog = models.ForeignKey(Catalog, null=False, on_delete=models.CASCADE)
    element_code = models.CharField(max_length=10, blank=False, validators=[validate_slug])
    value = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.element_code + self.value
