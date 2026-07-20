#!/usr/bin/env python3
"""Search modulo a large prime for a bounded-degree polynomial slice.

The derivation is
  E = a d/db + b d/dc + (b^2-2ac-1) d/dd + w d/dv.
This is only an experimental obstruction/certificate generator; any
positive answer must subsequently be checked over Q symbolically.
"""

import argparse
from itertools import product

MOD = 1000003


def monomials(max_degree):
    out = []
    for e in product(range(max_degree + 1), repeat=5):
        if sum(e) <= max_degree:
            out.append(e)
    return out


def add_term(vec, exp, coeff):
    coeff %= MOD
    if not coeff:
        return
    vec[exp] = (vec.get(exp, 0) + coeff) % MOD
    if vec[exp] == 0:
        del vec[exp]


def image(exp, w_terms):
    a, b, c, d, v = exp
    out = {}
    if b:
        e = (a + 1, b - 1, c, d, v)
        add_term(out, e, b)
    if c:
        e = (a, b + 1, c - 1, d, v)
        add_term(out, e, c)
    if d:
        add_term(out, (a, b + 2, c, d - 1, v), d)
        add_term(out, (a + 1, b, c + 1, d - 1, v), -2 * d)
        add_term(out, (a, b, c, d - 1, v), -d)
    if v:
        for we, wc in w_terms.items():
            e = (a + we[0], b + we[1], c + we[2], d + we[3], v - 1 + we[4])
            add_term(out, e, v * wc)
    return out


def scale_add(dst, src, factor):
    for key, val in src.items():
        add_term(dst, key, factor * val)


def reduce_vec(vec, combo, basis):
    while vec:
        pivot = max(vec)
        if pivot not in basis:
            return pivot
        bvec, bcombo = basis[pivot]
        factor = -vec[pivot] * pow(bvec[pivot], MOD - 2, MOD)
        scale_add(vec, bvec, factor)
        for key, val in bcombo.items():
            add_term(combo, key, factor * val)
    return None


def parse_w(name):
    table = {
        "c2": {(0, 0, 2, 0, 0): 1},
        "c3": {(0, 0, 3, 0, 0): 1},
        "c4": {(0, 0, 4, 0, 0): 1},
        "cd": {(0, 0, 1, 1, 0): 1},
        "d2": {(0, 0, 0, 2, 0): 1},
        "c2+d": {(0, 0, 2, 0, 0): 1, (0, 0, 0, 1, 0): 1},
        "c+d2": {(0, 0, 1, 0, 0): 1, (0, 0, 0, 2, 0): 1},
        "c2+cd": {(0, 0, 2, 0, 0): 1, (0, 0, 1, 1, 0): 1},
        "c2+d2": {(0, 0, 2, 0, 0): 1, (0, 0, 0, 2, 0): 1},
        "c2+d": {(0, 0, 2, 0, 0): 1, (0, 0, 0, 1, 0): 1},
        "1+hd": {
            (0, 0, 0, 0, 0): 1,
            (0, 4, 1, 1, 0): 1,
            (1, 2, 2, 1, 0): -4,
            (0, 2, 1, 1, 0): -2,
            (2, 0, 3, 1, 0): 4,
            (1, 0, 2, 1, 0): 4,
            (0, 0, 1, 1, 0): 1,
            (0, 3, 0, 2, 0): -1,
            (1, 1, 1, 2, 0): 2,
            (0, 1, 0, 2, 0): 1,
            (1, 0, 0, 3, 0): (MOD + 1) // 2,
        },
        "1+hd2": {
            (0, 0, 0, 0, 0): 1,
            (0, 4, 1, 2, 0): 1,
            (1, 2, 2, 2, 0): -4,
            (0, 2, 1, 2, 0): -2,
            (2, 0, 3, 2, 0): 4,
            (1, 0, 2, 2, 0): 4,
            (0, 0, 1, 2, 0): 1,
            (0, 3, 0, 3, 0): -1,
            (1, 1, 1, 3, 0): 2,
            (0, 1, 0, 3, 0): 1,
            (1, 0, 0, 4, 0): (MOD + 1) // 2,
        },
    }
    return table[name]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("w", choices=["c2", "c3", "c4", "cd", "d2", "c2+d", "c+d2", "c2+cd", "c2+d2", "1+hd", "1+hd2"])
    parser.add_argument("max_degree", type=int)
    args = parser.parse_args()

    basis = {}
    source = monomials(args.max_degree)
    for index, exp in enumerate(source):
        vec = image(exp, parse_w(args.w))
        if not vec:
            continue
        combo = {index: 1}
        pivot = reduce_vec(vec, combo, basis)
        if pivot is not None:
            inv = pow(vec[pivot], MOD - 2, MOD)
            vec = {key: val * inv % MOD for key, val in vec.items()}
            combo = {key: val * inv % MOD for key, val in combo.items()}
            basis[pivot] = (vec, combo)

    target = {(0, 0, 0, 0, 0): 1}
    target_combo = {}
    reduce_vec(target, target_combo, basis)
    print("FOUND_MOD_P" if not target else "NO_SLICE_IN_BOUND", args.w, args.max_degree)
    if not target:
        names = ("a", "b", "c", "d", "v")
        terms = []
        for index, coeff in sorted(target_combo.items()):
            coeff = (-coeff) % MOD
            signed = coeff if coeff <= MOD // 2 else coeff - MOD
            factors = [names[j] + ("^" + str(e) if e != 1 else "")
                       for j, e in enumerate(source[index]) if e]
            terms.append((signed, "*".join(factors) or "1"))
        print(terms)


if __name__ == "__main__":
    main()
