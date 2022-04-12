from itertools import permutations
class WaterjugSolver:
    """
    This class is created for solving the water jug problem.
    """

    def __init__(self,x,y,goal):
        """
        Initialization
        :param x:  represents the measurement of water jug1
        :param y: represents the measurement of water jug2
        :param goal: represents the measurement of goal
        """
        self.x = x
        self.y = y
        self.goal = goal
        self.s_space = []  # list for the possible state space
        self.goal_states = [] # list for the possible goal state
    def state_space(self):
        p_num = list(range(6))  # possible litres of water
        perm = list(permutations(p_num, 2))

        larger = self.x if self.x > self.y else self.y # larger stores jug with greater measurement
        for i in range(larger):
            perm.append((i,i))

        for element in perm:
            if element[0] > 3:
                continue
            else:
                self.s_space.append(element)
        return self.s_space

    def goal_state(self):
        for i in self.s_space:
            if i[0] + i[1] == self.goal:
                self.goal_states.append(i)

        return self.goal_states

    def solver(self):
        #Empty xl jug rule
        def empty_x(x,y):
            return (0,y)

        #Empty yl jug rule
        def empty_y(x,y):
            return (x,0)

        #Pour PL from x to y
        def pour_p_x_y(x,y,p):
            return (x - p, y + p)

        # Pour PL from x to y
        def pour_p_y_x(x,y,p):
            return (x + p, y - p)

        #fill x jug
        def fill_x(x,y):
            return (self.x, y)

        # fill x jug
        def fill_y(x,y):
            return (x, self.y)

        rules = [fill_y,pour_p_y_x,empty_x,pour_p_y_x,fill_y,pour_p_y_x,empty_x]
        steps = [] # represents steps for solving problem
        temp = 3
        state = (0,0) #initial state where both jugs are empty
        for rule in rules:
            if rule == pour_p_y_x:
                state = pour_p_y_x(state[0],state[1],temp)
                steps.append(state)
                temp -=  1
            else:
                state = rule(state[0],state[1])
                steps.append(state)
        count = 1
        print('-' * 10, "Solution", '-' * 10)
        for i in steps:
            print('-' * 20)
            print(f"Step {count}: {i}")
            count += 1
            print('-' * 20)

        # Tried for the General solution
        # for path in list(permutations(rules)):
        #     solution = []
        #     for i in range(len(path)):
        #         if path[i] == pour_p_y_x:
        #             state = path[i](0, 0,random.randint(0,3))
        #             solution.append(state)
        #         elif path[i] == pour_p_x_y:
        #             state = path[i](0, 0,random.randint(0,3))
        #             solution.append(state)
        #         else:
        #             state = path[i](0,0)
        #             solution.append(state)
        #     print(solution)

s = WaterjugSolver(3,5,4)
print('-'*20,"State Space",'-'*20)
print(s.state_space())
print('-'*20,"Possible Solution State",'-'*20)
print(s.goal_state())
s.solver()