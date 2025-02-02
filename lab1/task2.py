import random

class Environment:
    #random function used to update inital state of all the 5 servers
    def __init__(self):
        self.servers = {f"Server {i+1}": random.choice(["Underloaded", "Balanced", "Overloaded"]) for i in range(5)}

    def display_state(self):
        print("Server Loads:", self.servers)

    def adjust_load(self, overloaded, underloaded):
        self.servers[overloaded] = "Balanced"
        self.servers[underloaded] = "Balanced"

#agent simulation
class LoadBalancerAgent:
    def __init__(self, environment):
        self.environment = environment

    def balance_load(self):
        overloaded = [s for s in self.environment.servers if self.environment.servers[s] == "Overloaded"]
        underloaded = [s for s in self.environment.servers if self.environment.servers[s] == "Underloaded"]

        print("\nBalancing Load.")
        while overloaded and underloaded:
            self.environment.adjust_load(overloaded.pop(), underloaded.pop())

#running the simulation
env = Environment()
agent = LoadBalancerAgent(env)

print("Initial Server State:")
env.display_state()

agent.balance_load()

print("\nFinal Server State:")
env.display_state()
