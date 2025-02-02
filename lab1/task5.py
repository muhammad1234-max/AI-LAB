import random

class Environment:
    def __init__(self):
        self.rooms = {f"Room {i+1}": random.choice(["Needs Medicine", "No Delivery Needed"]) for i in range(5)}

    def display_state(self):
        print("Hospital State:", self.rooms)

    def deliver_medicine(self, room):
        self.rooms[room] = "Delivered"

#goal based agent implementation
class HospitalRobot:
    def __init__(self, environment):
        self.environment = environment

    def deliver_medicines(self):
        print("\nStarting Medicine Delivery...")
        for room, status in self.environment.rooms.items():
            if status == "Needs Medicine":
                print(f" Delivering Medicine to {room}")
                self.environment.deliver_medicine(room)


env = Environment()
robot = HospitalRobot(env)

print("Initial Hospital State:")
env.display_state()

robot.deliver_medicines()

print("\nFinal Hospital State:")
env.display_state()
