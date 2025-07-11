from parking_lot import ParkingLot
from vehicle_type import VehicleType

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