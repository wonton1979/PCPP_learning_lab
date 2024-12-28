class Tires:
    def __init__(self,size):
        self.size = size
        self.__pressure = 0

    @property
    def pressure(self):
        return self.__pressure

    def pump(self):
        if self.__pressure < 36:
            self.__pressure += 36 - self.__pressure
            print("The tires pressure pumped to the limit and ready to go.")
        else:
            print("The tires pressure is fine, you don't need to pump it.")

class Engine:
    def __init__(self,fuel_type):
        self.fuel_type = fuel_type
        self.engine_state = 'off'

    def start(self):
        self.engine_state = 'on'
        print(f"Engine is {self.engine_state}")

    def stop(self):
        self.engine_state = 'off'
        print("Engine is {self.engine_state}")

class Car:
    def __init__(self,VIN,tires,engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


city_tires = Tires(15)
off_road_tires = Tires(18)
electric_engine = Engine("Electric Engine")
petrol_engine = Engine("Petrol Engine")

city_car = Car(134557890,city_tires,electric_engine)
all_terrain_car = Car(788379793,off_road_tires,petrol_engine)

city_car.engine.start()
all_terrain_car.tires.pump()
print(all_terrain_car.tires.pressure)

