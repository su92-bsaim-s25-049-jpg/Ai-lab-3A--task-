# Model-Based Reflex Agent (Heater System)

class HeaterAgent:
    def __init__(self):
        self.previous_action = None  

    def decide(self, temperature):
    
        if temperature < 20:
            if self.previous_action != "ON":
                self.previous_action = "ON"
                print("Heater ON ")
            else:
                print("Heater already ON (no change)")

        else:
            if self.previous_action != "OFF":
                self.previous_action = "OFF"
                print("Heater OFF ")
            else:
                print("Heater already OFF (no change)")

agent = HeaterAgent()

temperatures = [18, 18, 22, 22, 19, 21]

for temp in temperatures:
    print("\nTemperature:", temp)
    agent.decide(temp)