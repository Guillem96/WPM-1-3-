class Clause:

    """
        cost: Integer, clause cost
        literals: Integer list, variables of clause
    """
    def __init__(self, cost, literals):
        self.cost = cost
        self.literals = literals

    def add(self, literal):
        return Clause(self.cost, self.literals.append(literal))

    def len(self):
        return len(set(map(abs, self.literals)))

    @staticmethod
    def clause_from_dimacs_line(line):
        line_split = line.split()
        cost = int(line_split[0])
        literals = map(int,line_split[1:-1])
        return Clause(cost, literals)

    def pretty_str(self):
        return "Cost: " + str(self.cost) + \
                " - Literals: [" +  ", ".join(self.literals)  + "]"

    # Overrides
    def __str__(self):
        return str(self.cost) + " " + " ".join(map(str,self.literals)) + " 0"
