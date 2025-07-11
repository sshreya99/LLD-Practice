from level import Level
from vehicle import Vehicle
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

