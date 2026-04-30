import heapq
from copy import deepcopy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Board:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n)

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = [
            ("Up", x - 1, y),
            ("Down", x + 1, y),
            ("Left", x, y - 1),
            ("Right", x, y + 1)
        ]

        for move_name, new_x, new_y in moves:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = deepcopy(self.state)
                # Swap blank with target tile
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

                successors.append(
                    Board(new_state, self, f"Move {new_state[x][y]} {move_name}", self.depth + 1)
                )

        return successors

    def __lt__(self, other):
        return False  # Required for heapq


# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(initial_state):
    start = Board(initial_state)

    open_list = []
    heapq.heappush(open_list, (0, start))

    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        visited.add(tuple(map(tuple, current.state)))

        for successor in current.generate_successors():
            state_tuple = tuple(map(tuple, successor.state))

            if state_tuple not in visited:
                f_cost = successor.depth + manhattan_distance(successor.state)
                heapq.heappush(open_list, (f_cost, successor))

    return None


def print_solution(goal_node):
    path = []
    current = goal_node

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    print("Solution Steps:\n")

    for i, step in enumerate(path):
        print(f"Step {i}:")
        step.display()
        if step.move:
            print(step.move)
        print("------------------")


# Example Initial State
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = a_star(initial_state)

if solution:
    print_solution(solution)
else:
    print("No solution found.")