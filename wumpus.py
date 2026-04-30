class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = [0, 0]   # Start position
        self.gold_pos = [2, 2]
        self.wumpus_pos = [1, 2]
        self.pits = [[3, 1], [2, 3]]
        self.has_gold = False
        self.alive = True

    def display(self):
        print("\nGrid World:")
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.agent_pos:
                    print("A", end=" ")
                elif [i, j] == self.gold_pos and not self.has_gold:
                    print("G", end=" ")
                elif [i, j] == self.wumpus_pos:
                    print("W", end=" ")
                elif [i, j] in self.pits:
                    print("P", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def move(self, direction):
        x, y = self.agent_pos

        if direction == "UP":
            x -= 1
        elif direction == "DOWN":
            x += 1
        elif direction == "LEFT":
            y -= 1
        elif direction == "RIGHT":
            y += 1
        else:
            print("Invalid move!")
            return

        if 0 <= x < self.size and 0 <= y < self.size:
            self.agent_pos = [x, y]
            print(f"Moved {direction}")
            self.check_status()
        else:
            print("Hit wall! Can't move.")

    def check_status(self):
        if self.agent_pos == self.wumpus_pos:
            print("💀 Eaten by Wumpus!")
            self.alive = False
        elif self.agent_pos in self.pits:
            print("💀 Fell into a pit!")
            self.alive = False
        elif self.agent_pos == self.gold_pos and not self.has_gold:
            print("✨ You found the gold!")

    def grab_gold(self):
        if self.agent_pos == self.gold_pos and not self.has_gold:
            self.has_gold = True
            print("🏆 Gold collected!")
        else:
            print("No gold here.")

    def sense(self):
        x, y = self.agent_pos
        breeze = False
        stench = False

        # Check adjacent cells
        directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

        for dx, dy in directions:
            if [dx, dy] in self.pits:
                breeze = True
            if [dx, dy] == self.wumpus_pos:
                stench = True

        if breeze:
            print("🌬 Breeze nearby (pit close)")
        if stench:
            print("💨 Stench nearby (Wumpus close)")
        if not breeze and not stench:
            print("😌 Safe cell")

    def is_game_over(self):
        return not self.alive or self.has_gold


# ----------- Run Example -----------
if __name__ == "__main__":
    world = GridWorld()
    
    print("Welcome to Grid World (Wumpus-like)!")
    
    while not world.is_game_over():
        world.display()
        world.sense()

        action = input("Enter action (UP/DOWN/LEFT/RIGHT/GRAB/QUIT): ").upper()

        if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            world.move(action)
        elif action == "GRAB":
            world.grab_gold()
        elif action == "QUIT":
            break
        else:
            print("Invalid action!")

    print("\nGame Over!")