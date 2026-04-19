from itertools import product

def parse_expr(expr):
    constraints = {}
    expr = expr.replace(" ", "")
    
    i = 0
    while i < len(expr):
        if expr[i] == 'b':
            idx = int(expr[i+1])
            if i+2 < len(expr) and expr[i+2] == "'":
                constraints[idx] = 0
                i += 3
            else:
                constraints[idx] = 1
                i += 2
        else:
            i += 1
    
    return constraints

def get_minterms(constraints, n = 8):
    all_vars = set(range(n))
    fixed_vars = set(constraints.keys())
    free_vars = list(all_vars - fixed_vars)

    minterms = []

    for bits in product([0, 1], repeat=len(free_vars)):
        val = [0]*n

        for k, v in constraints.items():
            val[k] = v

        for i, var in enumerate(free_vars):
            val[var] = bits[i]

        idx = int("".join(str(val[i]) for i in range(n - 1, -1, -1)), 2)
        minterms.append(idx)

    return sorted(minterms)
