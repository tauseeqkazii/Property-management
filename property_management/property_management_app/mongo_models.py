from djongo import models

class LeaseAgreement(models.Model):
    tenant_name = models.CharField(max_length=255)
    property_address = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return f'Lease Agreement for {self.tenant_name} at {self.property_address}'

class MaintenanceReport(models.Model):
    tenant_name = models.CharField(max_length=255)
    property_address = models.TextField()
    issue_date = models.DateField()
    description = models.TextField()
    resolution = models.TextField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return f'Maintenance Report for {self.tenant_name} at {self.property_address}'

    class Meta:
        verbose_name_plural = "Maintenance Reports"
