from itertools import product

def gate_to_minterms(gate):
    n = len(gate)
    
    fixed = {}
    free = []

    for i, v in enumerate(gate):
        if v == 1:
            fixed[i] = 1
        elif v == 0:
            fixed[i] = 0
        else:
            free.append(i)

    mins = []

    for comb in product([0,1], repeat = len(free)):
        bits = [0] * n

        for k, v in fixed.items():
            bits[k] = v

        for i, idx in enumerate(free):
            bits[idx] = comb[i]

        mins.append(int("".join(map(str, bits)), 2))

    return mins


def get_minterms(all_gates):
    result = set()

    for g in all_gates:
        result.update(gate_to_minterms(g))

    return sorted(result)