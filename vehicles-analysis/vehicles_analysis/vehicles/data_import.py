import csv
from .models import ICEVehicle, EVVehicle, HEVVehicle


def import_from_csv(file_path, vehicle_type):
    model_classes = {
        'ICEVehicle': ICEVehicle,
        'EVVehicle': EVVehicle,
        'HEVVehicle': HEVVehicle
    }

    if vehicle_type not in model_classes:
        raise ValueError(
            f'Такой тип машин {vehicle_type} в данной утилите не представлен. '
            f'Доступны только: {", ".join(model_classes.keys())}'
        )

    model_class = model_classes[vehicle_type]

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:

            if vehicle_type == 'ICEVehicle':
                model_class.objects.create(
                    name=row['name'],
                    price=float(row['price']),
                    fuel_type=row['fuel_type'],
                    fuel_consumption=float(row['fuel_consumption']),
                    production_co2=float(row['production_co2'])
                )
            elif vehicle_type == 'EVVehicle':
                model_class.objects.create(
                    name=row['name'],
                    price=float(row['price']),
                    battery_capacity=float(row['battery_capacity']),
                    energy_consumption=float(row['energy_consumption']),
                    production_co2=float(row['production_co2'])
                )
            elif vehicle_type == 'HEVVehicle':
                model_class.objects.create(
                    name=row['name'],
                    price=float(row['price']),
                    fuel_type=row.get('fuel_type'),
                    fuel_consumption=float(row['fuel_consumption']) if row.get('fuel_consumption') else None,
                    energy_consumption=float(row['energy_consumption']) if row.get('energy_consumption') else None,
                    production_co2=float(row['production_co2'])
                )
