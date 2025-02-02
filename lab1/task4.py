import random

#initializing the environment
class Environment:
    def __init__(self):
        self.components = {chr(65+i): random.choice(["Safe", "Low Risk", "High Risk"]) for i in range(9)}

    def display_state(self):
        print("System State:", self.components)

    def patch_component(self, component):
        if self.components[component] == "Low Risk":
            self.components[component] = "Safe"
            return "Patched"
        else:
            return "Requires Premium Service"

#utility based agent
class UtilitySecurityAgent:
    def __init__(self, environment):
        self.environment = environment

    def scan_and_patch(self):
        print("\nScanning System...")
        for component, status in self.environment.components.items():
            if status == "Low Risk":
                print(f" Patching {component} (Low Risk)")
                self.environment.patch_component(component)
            elif status == "High Risk":
                print(f" {component} has a High-Risk Vulnerability! Premium Service Required.")

#run the simulation
env = Environment()
agent = UtilitySecurityAgent(env)

print("Initial System Check:")
env.display_state()

agent.scan_and_patch()

print("\nFinal System Check:")
env.display_state()
