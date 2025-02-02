from smoosh.authorship.models import Authorship
from django.db import models
from django.conf import settings


class File(Authorship):
    """A file.

    This database model represents a file in the filesystem.
    """

    path = models.FilePathField(
        path=settings.LIBRARY_PATH,
        allow_files=True,
        allow_folders=False,
        unique=True,
    )

    device = models.CharField(
        max_length=20,
        help_text="Device that the file is from, according to the host OS.",
    )

    inode_number = models.CharField(
        max_length=20,
        help_text="An OS-dependent unique identifier for file within the context of "
        "the recorded device. On Unix-like systems, this is the inode number. On "
        "Windows, this is the file index.",
    )

    size = models.PositiveBigIntegerField(
        help_text="Size of the file (in bytes).",
    )

    hash = models.BinaryField(
        max_length=64,
        help_text="XXH128 hash of the file contents.",
        blank=True,
        null=True,
    )

    class Meta:
        default_related_name = "files"
        ordering = ["path"]
        indexes = [
            models.Index(fields=["path"]),
            models.Index(fields=["device", "inode_number"]),
        ]
