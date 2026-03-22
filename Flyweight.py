class CarModel:
    def __init__(self, brand: str, model: str, color: str, photo_url: str):
        self.brand = brand
        self.model = model
        self.color = color
        self.photo_url = photo_url


class CarModelFactory:
    _models = {}

    @classmethod
    def get_car_model(cls, brand: str, model: str, color: str, photo_url: str) -> CarModel:
        key = f"{brand}_{model}_{color}"

        if key not in cls._models:
            cls._models[key] = CarModel(brand, model, color, photo_url)

        return cls._models[key]


class Car:
    def __init__(self, plates: str, lat: float, lon: float, car_model: CarModel):
        self.plates = plates
        self.lat = lat
        self.lon = lon
        self.car_model = car_model  # Посилання на спільний об'єкт

    def update_location(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def get_info(self) -> str:
        return f"Авто [{self.plates}]: {self.car_model.color} {self.car_model.brand} {self.car_model.model} | Координати: ({self.lat}, {self.lon})"


if __name__ == "__main__":
    city_cars = []

    for i in range(3):
        model_renault = CarModelFactory.get_car_model("Renault", "Logan", "White", "/images/ren_log_w.png")
        car = Car(plates=f"BC000{i}PT", lat=50.45 + i * 0.03, lon=30.52, car_model=model_renault)
        city_cars.append(car)

    for i in range(2):
        model_toyota = CarModelFactory.get_car_model("Toyota", "Camry", "Black", "/images/toy_cam_b.png")
        car = Car(plates=f"BC999{i}AA", lat=50.40, lon=30.60 + i * 0.07, car_model=model_toyota)
        city_cars.append(car)

    print("Відображення на карті")
    for car in city_cars:
        print(car.get_info())

    print()
    print("Використання пам'яті")
    print(f"Всього автомобілів на карті: {len(city_cars)}")
    print(f"Об'єктів моделей у пам'яті: {len(CarModelFactory._models)}")