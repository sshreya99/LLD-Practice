from enum import Enum

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3

class Vehicle:
    def __init__(self, vehicle_type: VehicleType, vehicle_number):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number

class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.is_parked = False
        self.vehicle = None

    def park_vehicle(self, vehicle:Vehicle):
        if not self.is_parked:
            self.is_parked = True
            self.vehicle = vehicle
            return True
        return False
    
    def unpark_vehicle(self, vehicle:Vehicle):
        if self.is_parked and self.vehicle == vehicle:
            self.is_parked = False
            self.vehicle = None
            return True
        return False       

class Level:
    def __init__(self, level_number, parking_spot):
        self.level_number = level_number
        self.parking_spots: list[ParkingSpot] = [ParkingSpot(spot) for spot in range(parking_spot)]
    
        
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
                if spot.park_vehicle(vehicle):
                    return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.unpark_vehicle(vehicle):
                 return True
        return False
    
class ParkingLot:
    _instance = None
    def __init__(self):
        if ParkingLot._instance is not None:
           raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels : list[Level] = []
            
    @staticmethod      
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_levels(self, level_number, spots):
        self.levels.append(Level(level_number, spots))
    
    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
        
    def unpark_vehicle(self, vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
      
    def display_availability(self):
        for level in self.levels:
            print(f"Level {level.level_number} Availability:")
            for spot in level.parking_spots:
                print(f"Spot {spot.spot_number}: {'Available' if spot.is_parked == False else 'Occupied'}") 


class ParkingLotDemo:
    def run():
        parking_lot_obj = ParkingLot.get_instance()
        parking_lot_obj.add_levels(1, 10)
        parking_lot_obj.add_levels(2, 5)
        parking_lot_obj.add_levels(3, 6)
        car = {VehicleType.CAR, "ABC123"}
        truck = {VehicleType.TRUCK, "ABR123"}
        motorcycle = {VehicleType.MOTORCYCLE, "ABF123"}
        parking_lot_obj.park_vehicle(car)
        parking_lot_obj.park_vehicle(truck)
        parking_lot_obj.park_vehicle(motorcycle)

        parking_lot_obj.display_availability()
        parking_lot_obj.unpark_vehicle(car)
      
        parking_lot_obj.display_availability()



if __name__ == "__main__":
    ParkingLotDemo.run()