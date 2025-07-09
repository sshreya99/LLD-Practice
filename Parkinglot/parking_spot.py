from vehicle_type import VehicleType
from vehicle import Vehicle
class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.is_parked = False
        self.vehicle = None

        