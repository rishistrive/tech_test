from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ResourceCollection(Timestamp):
    building_csv = models.FileField(upload_to=f"building_data/csv")
    resource_csv = models.FileField(upload_to=f"meter_data/csv")
    resource_usage_csv = models.FileField(upload_to=f"half_hourly_data/csv")

    def __str__(self) -> str:
        return f"resource_collection_{self.pk}"
