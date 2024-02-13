class WashType:
    """Represents a wash type with its duration and cost."""
    def __init__(self, name, duration, cost):
        self.name = name
        self.duration = duration  # in minutes
        self.cost = cost

class Coin:
    """Represents a coin accepted by the washing machine."""
    ACCEPTED_VALUES = [10, 20, 50, 100]  # 10 cents, 20 cents, 50 cents, 1 dollar

    def __init__(self, value):
        if value in Coin.ACCEPTED_VALUES:
            self.value = value
        else:
            raise ValueError("Coin value not accepted.")

class WashingMachine:
    """Represents the washing machine."""
    def __init__(self):
        self.coins_credited = {
            "10-cent":0,
            "20-cent":0,
            "50-cent":0,
            "1-dollar":0
        }
        self.coins_earned = {
            "10-cent":0,
            "20-cent":0,
            "50-cent":0,
            "1-dollar":0
        }
        self.total_credited = 0
        self.current_wash_type = None
        self.total_earned = 0
        self.is_locked = False
        self.total_time_on = 0 
        self.wash_types = {
            "Quick":WashType("Quick Wash", 10, 200),
            "Mild":WashType("Mild Wash", 30, 250),
            "Medium":WashType("Medium Wash", 45, 420),
            "Heavy":WashType("Heavy Wash", 60, 600)
        }
    
    def calculate_total_credited(self):
        """Returns the total credited amount of the washing machine."""
        self.total_credited = 0
        for k, v in self.coins_credited.items():
            if k == "10-cent":
                self.total_credited += v * 10
            elif k == "20-cent":
                self.total_credited += v * 20
            elif k == "50-cent":
                self.total_credited += v * 50
            elif k == "1-dollar":
                self.total_credited += v * 100

    def calculate_total_earned(self):
        """Returns the total earned amount of the washing machine."""
        self.total_earned = 0
        for k, v in self.coins_earned.items():
            if k == "10-cent":
                self.total_earned += v * 10
            elif k == "20-cent":
                self.total_earned += v * 20
            elif k == "50-cent":
                self.total_earned += v * 50
            elif k == "1-dollar":
                self.total_earned += v * 100

    def accept_coin(self, coin):
        """Accepts a coin and updates the associated coin that is credited"""
        if coin.value == 10:
            self.coins_credited["10-cent"] += 1
        elif coin.value == 20:
            self.coins_credited["20-cent"] += 1
        elif coin.value == 50:
            self.coins_credited["50-cent"] += 1
        elif coin.value == 100:
            self.coins_credited["1-dollar"] += 1
        self.calculate_total_credited()
        # does nothing if coin with invalid value is inserted

    def select_wash_type(self, wash_type):
        """Allows the user to select a wash type"""
        if wash_type not in self.wash_types:
            raise ValueError("Invalid wash type selected.")
        self.current_wash_type = self.wash_types[wash_type]
        if self.total_credited < self.current_wash_type.cost:
            print("Insufficient funds for the selected wash type.")
            return False
        return True

    def start_wash(self):
        """Starts the washing process if balance is sufficient."""
        if self.current_wash_type and self.total_credited >= self.current_wash_type.cost:
            self.is_locked = True
            self.total_earned += self.current_wash_type.cost
            self.total_time_on += self.current_wash_type.duration
            self.total_credited -= self.current_wash_type.cost
            # Simulate washing process (omitted)
            self.is_locked = False
            print(f"Washing complete: {self.current_wash_type.name}")
            if self.total_credited > 0:
                self.refund()
        else:
            print("Insufficient balance or wash type not selected.")

    def refund(self):
        """Refunds the remaining balance to the user."""
        print(f"Refunding ${self.total_credited / 100:.2f}")
        self.coins_credited = {
            "10-cent":0,
            "20-cent":0,
            "50-cent":0,
            "1-dollar":0
        }
        self.total_credited = 0

    def display_statistics(self):
        """Displays quick statistics of the washing machine."""
        print(f"Total time on: {self.total_time_on} minutes")
        print(f"Total earned: ${self.total_earned}")

    def reset_statistics(self):
        """Resets the washing machine statistics."""
        self.total_time_on = 0
        self.total_earned = 0
        print("Statistics reset.")
