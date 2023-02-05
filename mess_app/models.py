from django.contrib import admin  # noqa: F401
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(
        verbose_name="Name",
        max_length=254,
        help_text="(e.g. 'Anna' or 'Anna-Claire')",
    )

    last_name = models.CharField(
        verbose_name="Surname",
        max_length=254,
        help_text="(e.g. 'Stopford' or 'Stopford-Sackville')",
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        help_text="(A valid email address, please.)",
    )

    class Meta:
        ordering = ['last_name', 'first_name', 'email']

    def __str__(self):
        return f"{self.first_name}_{self.last_name} ({self.email})"


class Logger(models.Model):
    # 1
    timestamp = models.DateTimeField(
        verbose_name="Created Time",
        auto_now_add=True,
        help_text="(The date and time when Log was created.)",
    )

    # 2
    path = models.URLField(
        verbose_name="The PATH",
        max_length=199,
        help_text="The PATH of the Request.",
    )

    # 3
    METHOD_CHOICES = (
            ("GET", 'GET'),
            ("POST", 'POST'),
            ("HEAD", "HEAD"),
            ("PUT", "PUT"),
            ("DELETE", "DELETE"),
            ("CONNECT", "CONNECT"),
            ("OPTIONS", "OPTIONS"),
            ("TRACE", "TRACE"),
            ("PATCH", "PATCH"),
    )

    method = models.CharField(
        verbose_name="The Method",
        max_length=7,
        choices=METHOD_CHOICES,
        help_text="A method (GET, POST, others).",
    )

    # 4
    request_data = models.JSONField(
        verbose_name="Request data in JSON",
        null=True,
    )

    # 5
    run_time = models.DecimalField(
        verbose_name="Execution time of the request.",
        max_digits=10,
        decimal_places=7,
    )

    class Meta:
        ordering = ['timestamp', 'path', 'method']

    def __str__(self):
        return f"{self.timestamp}_{self.path} ({self.method})"
