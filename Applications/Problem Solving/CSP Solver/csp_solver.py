from itertools import combinations, permutations
class CSP_Solver:
    """
    This CSP Solver solves with only two addends.
    """
    def __init__(self):
        self.addend1 = input('Enter first addend:')
        self.addend2 = input("Enter second addend:")
        self.sum = input("Enter the sum:")
        self.vars = set(self.addend1 + self.addend2 + self.sum)
        self.var_len = len(self.vars)
    def replacements(self):
        for comb in combinations(range(10), self.var_len):
            for perm in permutations(comb):
                if perm[0] != 0:
                    yield dict(zip(self.vars, perm))


    def solver(self):
        for replacement in self.replacements():
            f = lambda x: sum(replacement[e] * 10**i for i, e in enumerate(x[::-1]))
            if f(self.addend1) + f(self.addend2) == f(self.sum):
                print(f'{self.addend1} + {self.addend2} = {self.sum} \n{f(self.addend1)} + {f(self.addend2)} = {f(self.sum)}')

if __name__ == "__main__":
    s = CSP_Solver()
    s.solver()