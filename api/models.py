from django.core.validators import validate_slug
from django.db import models


class NonStrippingTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)


class Catalog(models.Model):
    class Meta:
        unique_together = (('fullname', 'version'),)
    fullname = NonStrippingTextField()
    shortname = NonStrippingTextField()
    description = NonStrippingTextField()
    version = models.CharField(max_length=10, blank=False)
    start_date = models.DateField("Version start day")

    def __str__(self):
        return f"{self.fullname}.{self.version}"


class Element(models.Model):
    class Meta:
        unique_together = (('catalog', 'element_code'),)
    catalog = models.ForeignKey(Catalog, null=False, on_delete=models.CASCADE)
    element_code = models.CharField(max_length=10, blank=False, validators=[validate_slug])
    value = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.element_code + self.value
