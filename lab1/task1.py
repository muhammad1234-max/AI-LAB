import random

#creating the environment
class Environment:
    #using a random function to allot either safe or vulnerable for the 9 components of the system
    def __init__(self):
        self.components = {chr(65+i): random.choice(["Safe", "Vulnerable"]) for i in range(9)}
    
    def display_state(self):
        print("System State:", self.components)

    def scan_component(self, component):
        return self.components[component]

    def patch_component(self, component):
        self.components[component] = "Safe"

#the agent
class SecurityAgent:
    def __init__(self, environment):
        self.environment = environment
        self.vulnerable_components = []

    def scan_system(self):
        print("\nScanning System...")
        for component in self.environment.components:
            status = self.environment.scan_component(component)
            if status == "Vulnerable":
                print(f" {component} is Vulnerable!")
                self.vulnerable_components.append(component)
            else:
                print(f" {component} is Safe")

    def patch_vulnerabilities(self):
        print("\nPatching Vulnerabilities...")
        for component in self.vulnerable_components:
            self.environment.patch_component(component)
            print(f" Patched {component}")

#running Simulation
env = Environment()
agent = SecurityAgent(env)

print("Initial System Check:")
env.display_state()

agent.scan_system()
agent.patch_vulnerabilities()

print("\nFinal System Check:")
env.display_state()
