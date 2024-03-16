import random

class Ant:
    def __init__(self, colony):
        self.colony = colony
        self.health = 100
    
    def move(self):
        # Simulate ant movement
        # For simplicity, assume ants move randomly within the colony
        self.colony.move_ant(self, random.choice(self.colony.grid))

    def get_infected(self):
        # Simulate ant getting infected
        self.health -= 20
    
    def heal(self):
        # Simulate ant healing
        self.health += 10

class Colony:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [(x, y) for x in range(width) for y in range(height)]
        self.ants = [Ant(self) for _ in range(10)]
        self.disease_spread = 0.1
    
    def move_ant(self, ant, position):
        # Simulate ant movement
        # For simplicity, assume ants move to a new random position
        self.grid.remove(position)
        new_position = random.choice(self.grid)
        self.grid.append(position)
    
    def spread_disease(self):
        # Simulate disease spread
        for ant in self.ants:
            if random.random() < self.disease_spread:
                ant.get_infected()
    
    def heal_ants(self):
        # Simulate ant healing
        for ant in self.ants:
            ant.heal()
    
    def simulate_day(self):
        # Simulate a day in the colony
        self.move_ants()
        self.spread_disease()
        self.heal_ants()
