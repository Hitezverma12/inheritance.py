class vechile:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vechile):
    pass

school_bus = Bus("School Volvo", 180, 12)
print("Vechile Name:", school_bus.name,"speed:", school_bus.max_speed, "mileage:", school_bus.mileage)
