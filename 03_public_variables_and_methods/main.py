class Car:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

mycar = Car("Toyota")
print(mycar.brand)
mycar.start()