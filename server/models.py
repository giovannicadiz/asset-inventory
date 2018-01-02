from django.db import models

# Create your models here.
class Server(models.Model):
    # general
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    dns = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    domain_role = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    dynamic_ip = models.CharField(max_length=255)
    # hardware
    asset_type = models.CharField(max_length=255)
    hardware = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    warranty_status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # operating system
    operating_system = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    last_boot = models.CharField(max_length=255)
    hardware_agent = models.CharField(max_length=255)
    # owner
    business_unit = models.CharField(max_length=255)

    Argentina = 'ARGENTINA'
    Bolivia = 'BOLIVIA'
    Brasil = 'BRASIL'
    Chile = 'CHILE'
    Colombia = 'COLOMBIA'
    Ecuador = 'ECUADOR'
    Paraguay = 'PARAGUAY'
    Peru = 'PERU'
    Uruguay = 'URUGUAY'
    Venezuela = 'Venezuela'

    COUNTRY_CHOICES = (
        (Argentina, 'ARGENTINA'),
        (Bolivia, 'BOLIVIA'),
        (Brasil, 'BRASIL'),
        (Chile, 'CHILE'),
        (Colombia, 'COLOMBIA'),
        (Ecuador, 'ECUADOR'),
        (Paraguay, 'PARAGUAY'),
        (Peru, 'PERU'),
        (Uruguay, 'URUGUAY'),
        (Venezuela, 'VENEZUELA'),
    )
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=255)

    def __str__(self):
        return (u'%s ' % self.host_name)
