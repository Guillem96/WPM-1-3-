from Formula import Formula
from Clause import Clause

#converts a soft clause into a soft clause with 1 literal and a list of hard clauses of lenght 3
def convert_soft(f,soft):
    new_literal=f.create_literal()
    new_soft=(soft.cost,new_literal * (-1) ) # (!b,soft_cost)
    soft.add(new_literal)
    new_hard=(f.hard_cost,soft.literals)
    hardslist = convert_hard(f,new_hard)
    return [new_soft] + hardslist


#converts a hard clause of maximum lenght N into hard clausules of maximum lenght 3
def convert_hard(f,hard):
    clause = Clause(f.hard_cost,[])
    clause_list = []
    literals_left=len(hard.literals)
    for literal in hard.literals:

        if clause.lenght == 2:

            if literals_left == 1:
                clause.add(literal)

            else:
                literal_aux=f.create_literal()
                clause.add(literal_aux)
                clause_list+=[clause]
                clause = Clause(f.hard_cost,[literal_aux * (-1)])
                clause.add(literal)
                literals_left-=1

        elif clause.lenght == 1:
            clause.add(literal)
            literals_left-=1

        elif clause.lenght == 0:
            clause.add(literal)
            literals_left-=1


    return clause_list + [clause]

if __name__ == '__main__':
    f = Formula()
    f.read_file('dimacs.txt')
    new_formula = Formula(f.num_literals,f.hard_cost,[])
    for soft_clause in f.soft_clauses:
        new_formula.add_clauses(convert_soft(new_formula,soft_clause))
    for hard_clauses in f.hard_clauses:
        new_formula.add_clauses(convert_hard(new_formula,hard_clauses))
    print str(new_formula)
