from parking_spot import ParkingSpot

class Level:
    def __init__(self, level_number, parking_spot):
        self.level_number = level_number
        self.parking_spots: list[ParkingSpot] = [ParkingSpot(spot) for spot in range(parking_spot)]
    
        
    # end def