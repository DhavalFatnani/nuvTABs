class Room:
    def __init__(self):
        self.room = None
        self.roomID = None
        self.seatingCapacity = None
        self.roomAvailability = None
        self.roomType = None

    def get_Room(self):
        self.room = {
            "roomID": self.roomID,
            "roomCapacity": self.seatingCapacity,
            "roomAvailability": self.roomAvailability,
            "roomType": self.roomType
        }
        return self.room

    def set_Room(self, rID, rCapacity, rAvailability, rType):
        self.roomID = rID
        self.seatingCapacity = rCapacity
        self.roomAvailability = rAvailability
        self.roomType = rType
