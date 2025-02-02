import random

#more or less same code like the previous questions so i dont have to add comments
class Environment:
    def __init__(self):
        self.backups = {f"Backup {i+1}": random.choice(["Completed", "Failed"]) for i in range(5)}

    def display_state(self):
        print("Backup Status:", self.backups)

    def retry_backup(self, backup):
        self.backups[backup] = "Completed"

class BackupAgent:
    def __init__(self, environment):
        self.environment = environment

    def retry_failed_backups(self):
        print("\nRetrying Failed Backups...")
        for backup, status in self.environment.backups.items():
            if status == "Failed":
                print(f" Retrying {backup}...")
                self.environment.retry_backup(backup)

env = Environment()
agent = BackupAgent(env)

print("Initial Backup State:")
env.display_state()

agent.retry_failed_backups()

print("\nFinal Backup State:")
env.display_state()
