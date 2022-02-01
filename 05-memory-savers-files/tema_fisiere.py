import os.path
import csv
import json

OUTPUT_DIR = 'output_data'
INPUT_FILE = 'input.csv'


def clean_old_files():
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # clean OUTPUT_DIR
    for file in os.listdir(OUTPUT_DIR):
        os.remove(os.path.join(OUTPUT_DIR, file))


def read_cars():
    cars = []
    with open(INPUT_FILE) as input_file:
        cars_reader = csv.reader(input_file, delimiter=',')
        for car in cars_reader:
            car_dict = {
                'id': id(car),
                'brand': car[0],
                'model': car[1],
                'hp': int(car[2]),
                'price': int(car[3])
            }
            cars.append(car_dict)

    return cars


def filter_cars_by_type(cars):
    car_types = {
        'slow_cars': filter(lambda c: c['hp'] < 120, cars),
        'fast_cars': filter(lambda c: 120 <= c['hp'] < 180, cars),
        'sport_cars': filter(lambda c: 180 <= c['hp'], cars),
        'cheap_cars': filter(lambda c: c['price'] < 1000, cars),
        'medium_cars': filter(lambda c: 1000 <= c['price'] < 5000, cars),
        'expensive_cars': filter(lambda c: 5000 <= c['price'], cars)
    }

    for car in cars:
        brand = car['brand'].lower()
        brand_cars = car_types.get(brand, [])
        brand_cars.append(car)
        car_types[brand] = brand_cars

    return car_types


def save_csv_file(filename, cars):
    with open(os.path.join(OUTPUT_DIR, filename), 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',')
        for car in cars:
            csv_writer.writerow(car.values())


def save_json_file(filename, cars):
    with open(os.path.join(OUTPUT_DIR, filename), 'w') as output_file:
        json.dump(list(cars), output_file)


def save_csv_files(car_types):
    for car_type, cars in car_types.items():
        save_csv_file(f"{car_type}.csv", cars)


def save_json_files(car_types):
    for car_type, cars in car_types.items():
        save_json_file(f"{car_type}.json", cars)


if __name__ == '__main__':
    clean_old_files()
    cars = read_cars()
    car_types = filter_cars_by_type(cars)
    save_csv_files(car_types)
    save_json_files(car_types)
