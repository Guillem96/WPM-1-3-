from Formula import Formula

#converts a soft clause into a soft clause with 1 literal and a list of hard clauses of lenght 3
def convert_soft(soft):
    new_literal=DimacsC.create_next_literal()
    new_soft=(soft.cost,new_literal * (-1) )
    new_hard=(DimacsC.hard_cost,soft.add(new_literal))
    hardslist = convert_hard(new_hard)
    return [new_soft] + hardslist


#converts a hard clause of maximum lenght N into hard clausules of maximum lenght 3
def convert_hard(hard):
    clause = Clause(DimacsC.hard_cost,[])
    clause_list = []
    literals_left=clause.lenght()
    for literal in hard.literals:

        if clause.lenght == 2:

            if literals_left == 1:
                clause=clause.add(literal)

            else:
                current_aux=DimacsC.create_next_literal()
                clause=clause.add(current_aux)
                clause_list+=[clause]
                clause = Clause(DimacsC.hard_cost,[current_aux * (-1)])
                clause=clause.add(literal)
                literals_left-=1

        elif clause.lenght == 1:
            clause=clause.add(literal)
            literals_left-=1

        elif clause.lenght == 0:
            clause=clause.add(literal)
            literals_left-=1


    return clause_list + [clause]

if __name__ == '__main__':
    f = Formula('dimacs.txt')
    print str(f)
