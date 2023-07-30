from django.contrib import admin
from .models import *


admin.site.register(ModelEngine)
admin.site.register(ModelTechnique)
admin.site.register(ModelTransmission)
admin.site.register(ModelDriveAxle)
admin.site.register(ModelSteerableBridge)
admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Reclamation)
admin.site.register(ServiceCompany)
admin.site.register(MaintenanceKind)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
