from Clause import Clause

class Formula:
    """ File format
        p wcnf 4 5 15
        15 1 -2 4 0
        15 -1 -2 3 0
        1 -2 -4 0
        1 -3 2 0
        1 1 3 0
    """

    def __init__(self, file_path):
        self.soft_clauses = []
        self.hard_clauses = []
        self.num_literals = 0
        self.hard_cost = 0
        self.aux_count = 0

        self.__read_file(file_path)

    def __read_file(self, file_path):
        for line in open(file_path):
            if "wcnf" in line: # first line
                # Get num
                self.num_literals = int(line.split()[2])
                # Get hard_cost
                self.hard_cost = int(line.split()[4])
            else:
                cost = int(line.split()[0])
                if cost == self.hard_cost:   # if hard clause
                    self.hard_clauses.append(Clause.clause_from_dimacs_line(line))
                else:
                    self.soft_clauses.append(Clause.clause_from_dimacs_line(line))

        self.aux_count = self.num_literals


    def create_literal(self):
        self.aux_count += 1
        return self.aux_count


    def __str__(self):
        # calculate num literals
        num_literals = self.aux_count

        # Calculate num_clauses
        num_clauses = len(self.hard_clauses) + len(self.soft_clauses)

        # Get hard_cost
        hard_cost = self.hard_clauses[0].cost

        # Format first line of dimacs
        f_line = "p wcnf " + str(self.num_literals) + " " \
                    + str(num_clauses) + " " \
                    + str(self.hard_cost) + "\n"
        # Fomrat soft clauses
        soft_clauses = "\n".join(map(str, self.soft_clauses)) + "\n"
        # Format hard claues
        hard_clauses = "\n".join(map(str, self.hard_clauses))
        return f_line + soft_clauses + hard_clauses
