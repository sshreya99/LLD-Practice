from parking_spot import ParkingSpot
from vehicle import Vehicle
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