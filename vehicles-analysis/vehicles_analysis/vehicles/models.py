from django.db import models


class Vehicle(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена (руб)")
    production_co2 = models.FloatField(
        verbose_name="Выбросы CO₂ при производстве (кг)",
        help_text="Учитывает производство кузова, батареи и т.д."
    )
    maintenance_per_km = models.FloatField(
        verbose_name="Стоимость ТО (руб/км)",
        default=0.5
    )
    recycle_cost = models.FloatField(
        verbose_name="Стоимость утилизации (руб)",
        default=30000
    )

    def __str__(self):
        return self.name

class ICEVehicle(Vehicle):
    fuel_type = models.CharField(
        max_length=20,
        choices=[('petrol', 'Бензин'), ('diesel', 'Дизель')],
        verbose_name="Тип топлива"
    )
    fuel_consumption = models.FloatField(
        verbose_name="Расход топлива (л/100 км)"
    )

    class Meta:
        verbose_name = "Автомобиль с ДВС"
        verbose_name_plural = "Автомобили с ДВС"

class EVVehicle(Vehicle):
    battery_capacity = models.FloatField(
        verbose_name="Ёмкость батареи (кВт·ч)"
    )
    energy_consumption = models.FloatField(
        verbose_name="Энергопотребление (кВт·ч/100 км)"
    )

    class Meta:
        verbose_name = "Электромобиль"
        verbose_name_plural = "Электромобили"

class HEVVehicle(Vehicle):
    fuel_consumption = models.FloatField(
        verbose_name="Расход топлива (л/100 км)",
        null=True,
        blank=True
    )
    energy_consumption = models.FloatField(
        verbose_name="Энергопотребление (кВт·ч/100 км)",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Гибридный автомобиль"
        verbose_name_plural = "Гибридные автомобили"