from pydantic import BaseModel

class Car(BaseModel):
    id: int
    brand: str
    model: str
    cost: int

cars_list = [
    Car(
        id = 1,
        brand = "Toyota",
        model = "Tundra",
        cost = 6000000
    ),
    Car(
        id=2,
        brand = "Dodge",
        model = "Viper",
        cost = 7000000
    ),
    Car(
        id=3,
        brand = "Lamborghini",
        model = "Murciélago",
        cost = 30000000
    ),
    Car(
        id=4,
        brand = "Mercedes Benz",
        model = "G63",
        cost = 9000000
    ),
    Car(
        id=5,
        brand = "BMW",
        model = "M5",
        cost = 8500000
    ),
]