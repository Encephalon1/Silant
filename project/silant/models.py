from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from datetime import date
from django.urls import reverse


class DirectoryDetails(models.Model):
    DETAILS_CHOICES = [
        ('TE', 'Модель техники'),
        ('EN', 'Модель двигателя'),
        ('TR', 'Модель трансмиссии'),
        ('DA', 'Модель ведущего моста'),
        ('SB', 'Модель управляемого моста'),
    ]
    detail = models.CharField(max_length=2, choices=DETAILS_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ModelTechnique(DirectoryDetails):
    detail = 'TE'


class ModelEngine(DirectoryDetails):
    detail = 'EN'


class ModelTransmission(DirectoryDetails):
    detail = 'TR'


class ModelDriveAxle(DirectoryDetails):
    detail = 'DA'


class ModelSteerableBridge(DirectoryDetails):
    detail = 'SB'


class DirectoryMaintenance(models.Model):
    DIRECTORIES = [
        ('KM', 'Вид ТО'),
        ('FN', 'Характер отказа'),
        ('RM', 'Способ восстановления'),
    ]
    directory_name = models.CharField(max_length=2, choices=DIRECTORIES)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class MaintenanceKind(DirectoryMaintenance):
    directory_name = 'KM'


class FailureNode(DirectoryMaintenance):
    directory_name = 'FN'


class RecoveryMethod(DirectoryMaintenance):
    directory_name = 'RM'


class ServiceCompany(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    factory_car_num = models.CharField(primary_key=True, max_length=255)
    technique_model = models.ForeignKey(ModelTechnique, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(ModelEngine, on_delete=models.CASCADE)
    factory_engine_num = models.CharField(max_length=255)
    transmission_model = models.ForeignKey(ModelTransmission, on_delete=models.CASCADE)
    factory_transmission_num = models.CharField(max_length=255)
    drive_axle_model = models.ForeignKey(ModelDriveAxle, on_delete=models.CASCADE)
    factory_drive_axle_num = models.CharField(max_length=255)
    steerable_bridge_model = models.ForeignKey(ModelSteerableBridge, on_delete=models.CASCADE)
    factory_steerable_bridge_num = models.CharField(max_length=255)
    supply_contract = models.CharField(max_length=100, blank=True, default=None)
    date_of_shipment = models.DateField(auto_now=True)
    consignee = models.CharField(max_length=255, blank=True, default=None)
    delivery_address = models.CharField(max_length=255, blank=True, default=None)
    equipment = models.CharField(max_length=255, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        get_latest_by = 'date_of_shipment'
        ordering = ['technique_model', 'engine_model', 'transmission_model', 'drive_axle_model',
                    'steerable_bridge_model']

    def __str__(self):
        return self.factory_car_num


class Maintenance(models.Model):
    kind_of_maintenance = models.ForeignKey(MaintenanceKind, on_delete=models.CASCADE)
    date_of_maintenance = models.DateField(auto_now=True)
    running_time = models.IntegerField()
    work_order = models.CharField(max_length=255)
    date_work_order = models.DateField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'date_of_maintenance'
        ordering = ['kind_of_maintenance', 'car', 'service_company']

    def __str__(self):
        return self.kind_of_maintenance


class Reclamation(models.Model):
    date_of_rejection = models.DateField(default=date.today)
    running_time = models.IntegerField()
    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE)
    failure_description = models.TextField()
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE)
    used_spare_parts = models.CharField(max_length=255)
    recovery_date = models.DateField(auto_now=True)
    machine_downtime = F(recovery_date) - F(date_of_rejection)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'date_of_rejection'
        ordering = ['failure_node', 'recovery_method', 'service_company']

    def __str__(self):
        return self.failure_node.name
