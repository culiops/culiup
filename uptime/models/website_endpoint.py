from uptime.models import Base, PeopleManager
from django.db import models


class WebsiteEndpoint(Base):
    STATUS_CHOICES = (
        ("UP", "UP"),
        ("DOWN", "DOWN"),
        ("PROGRESS", "PROGRESS"),
    )

    UP_STATUS_CHOICES = [
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        226,
        300,
        301,
        302,
        303,
        304,
        305,
        306,
        307,
        308,
    ]

    DOWN_STATUS_CHOICES = [
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511,
        520,
        521,
        522,
        523,
        524,
        525,
        526,
        527,
        530,
        598,
        599,
    ]

    HTTP_METHOD_CHOICES = (
        ("GET", "GET"),
        ("POST", "POST"),
        ("PUT", "PUT"),
        ("DELETE", "DELETE"),
        ("HEAD", "HEAD"),
        ("OPTIONS", "OPTIONS"),
        ("PATCH", "PATCH"),
    )

    CHECK_INTERVAL_CHOICES = (
        (30, "30 seconds"),
        (60, "1 minute"),
        (300, "5 minutes"),
        (600, "10 minutes"),
    )

    name = models.CharField(max_length=200)
    url = models.URLField()
    check_interval = models.SmallIntegerField(
        choices=CHECK_INTERVAL_CHOICES, default=60
    )
    check_timeout = models.SmallIntegerField(default=60)
    tries_to_check = models.SmallIntegerField(default=3)
    is_ssl_check = models.BooleanField(default=True)
    is_domain_check = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PROGRESS")
    up_statuses = models.JSONField(default=list)
    down_statuses = models.JSONField(default=list)
    category = models.CharField(max_length=200, blank=True, null=True)
    keywords = models.JSONField(default=list)
    http_method = models.CharField(
        max_length=10, choices=HTTP_METHOD_CHOICES, default="GET"
    )

    objects = models.Manager()
    people = PeopleManager()

    def __str__(self):
        return self.name

    def update_status(self, status):
        self.status = status
        self.save()

    def inactive(self):
        self.is_active = False
        self.save()

    def active(self):
        self.is_active = True
        self.save()

    def check_ssl(self):
        self.is_ssl_check = True
        self.save()

    def uncheck_ssl(self):
        self.is_ssl_check = False
        self.save()

    def check_domain(self):
        self.is_domain_check = True
        self.save()

    def uncheck_domain(self):
        self.is_domain_check = False
        self.save()
