class environment:
    def __init__(self):
        self.location_status = {"A": "dirty", "B": "clean"}
        self.agent_location = "A"

    def get_percept(self):
        return self.agent_location, self.location_status[self.agent_location]

    def execute_action(self, action):
        if action == "suck":
            self.location_status[self.agent_location] = "clean"
        elif action == "right" and self.agent_location == "A":
            self.agent_location = "B"
        elif action == "left" and self.agent_location == "B":
            self.agent_location = "A"

class intelligentagent:
    def decision_function(self, percept):
        location, status = percept
        if status == "dirty":
            return "suck"
        elif location == "A":
            return "right"
        elif location == "B":
            return "left"

def run_simulation(steps=4):
    env = environment()
    agent = intelligentagent()
    print(f"Initial environment: {env.location_status}, agent at: {env.agent_location}\n")
    
    for step in range(1, steps + 1):
        percept = env.get_percept()
        action = agent.decision_function(percept)
        env.execute_action(action)
        
        print(f"Step {step}:")
        print(f"  Percept -> Location: {percept[0]}, Status: {percept[1]}")
        print(f"  Action  -> {action}")
        print(f"  New State -> {env.location_status}, Agent at: {env.agent_location}\n")

if __name__ == "__main__":
    run_simulation()
    
