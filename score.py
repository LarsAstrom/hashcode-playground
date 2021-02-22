from dataparser import *
from collections import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    # TODO: implement
    D = ni(itr)
    assert 1<=D<=ns.T2+ns.T3+ns.T4
    assert D+1<=len(out.split('\n'))<=D+2
    out = 0
    used_pizzas = set()
    for _ in range(D):
        L = nl(itr)
        assert len(L) == L[0]+1
        L = L[1:]
        ingreds_team = []
        for p_id in L:
            assert p_id not in used_pizzas
            assert 0<=p_id<ns.M
            used_pizzas.add(p_id)
            ingreds_team += ns.pizzas[p_id]['ingredients']
        out += len(set(ingreds_team))**2
    return out
