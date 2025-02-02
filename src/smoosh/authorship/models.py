from django.db import models
from django.conf import settings


class Authorship(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+"
    )

    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
