from vehicle_type import VehicleType
from vehicle import Vehicle
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