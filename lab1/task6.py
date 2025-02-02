class Environment:
    #initializing Grid
    #just because i have used the flame icon please dont assume i have used gpt i added it myself after taking refrence from gpt :)
    def __init__(self):
        self.grid = {
            'a': "Safe", 'b': "Safe", 'c': "🔥",
            'd': "Safe", 'e': "🔥", 'f': "Safe",
            'g': "Safe", 'h': "Safe", 'j': "🔥"
        }

    def display_grid(self):
        print("\nCurrent Grid:")
        print(f"{self.grid['a']} | {self.grid['b']} | {self.grid['c']}")
        print(f"{self.grid['d']} | {self.grid['e']} | {self.grid['f']}")
        print(f"{self.grid['g']} | {self.grid['h']} | {self.grid['j']}")

    def extinguish_fire(self, room):
        if self.grid[room] == "🔥":
            self.grid[room] = "Safe"

class FirefightingRobot:
    def __init__(self, environment):
        self.environment = environment
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def extinguish_fires(self):
        print("\nStarting Fire Extinguishing...")
        for room in self.path:
            if self.environment.grid[room] == "🔥":
                print(f" Extinguishing fire in {room}")
                self.environment.extinguish_fire(room)
            self.environment.display_grid()

env = Environment()
robot = FirefightingRobot(env)

print("Initial Grid State:")
env.display_grid()

robot.extinguish_fires()

print("\nFinal Grid State:")
env.display_grid()
