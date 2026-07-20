# Audit of the `E=D+phi(h) partial_v` candidate

Let `k` be algebraically closed of characteristic zero and put

```
P = k[a,b,c,d],
q = b^2-2ac-1,
D(a)=0, D(b)=a, D(c)=b, D(d)=q,
r = ad-qb,
h = q^2c-qbd+ad^2/2.
```

Then `q,r,h` are `D`-invariant and

```
r^2 = 2ah + q^2(q+1).                       (1)
```

The following gives the required obstruction.

## Lemma (a nonzero level of `h`)

Fix `H in k^*` and let `A_H=P/(h-H)`, with the LND induced by `D`.
Then

1. `ker(D|A_H)=k[q,r]`;
2. the invariant morphism
   `pi_H: Spec(A_H) -> A^2_(q,r)` has image
   `A^2\{(0,0)}`;
3. over that image it is a Zariski locally trivial `Ga`-torsor;
4. `D|A_H` has no slice, and neither does its coefficientwise
   extension to `A_H[v]`.

### Proof

On the level `h=H`, relation (1) expresses

```
a = (r^2-q^2(q+1))/(2H).                    (2)
```

Moreover `h=q(qc-bd)+ad^2/2` belongs to `(a,q)`.  Hence `(a,q)=A_H`:
indeed `H=h-(h-H)` belongs to `(a,q,h-H)`.  Thus `Spec(A_H)` is covered
by the two principal opens `D(a)` and `D(q)`.

On `D(a)`, set `t=b/a`.  Direct substitution gives an isomorphism of
differential algebras

```
(A_H)_a = k[q,r]_a[t],       D(t)=1,         (3)
```

where `a` on the right means the polynomial in (2).  The inverse
formulas are

```
b=at,
d=r/a+qt,
c=at^2/2-(q+1)/(2a).
```

On `D(q)`, set `u=d/q`.  Similarly

```
(A_H)_q = k[q,r]_q[u],       D(u)=1,         (4)
```

with inverse formulas

```
a=(r^2-q^2(q+1))/(2H),
d=qu,
b=au-r/q,
c=H/q^2+au^2/2-ru/q.
```

The defining formulas for `q,r,h` verify both inverse maps.  In
particular both localizations are domains.  Since `(a,q)=A_H`, the map
from `A_H` to their product is injective; the common overlap is
nonempty, so `A_H` is a domain as well.

Equations (3) and (4) imply that a global invariant restricts to an
element of `k[q,r]_a` and to an element of `k[q,r]_q`.  On the overlap
the two restrictions agree in `k(q,r)`.  Since

```
gcd(q,a)=1 in k[q,r]
```

(reduce (2) modulo `q`, where it is the nonzero scalar multiple
`r^2/(2H)`), factoriality gives

```
k[q,r]_a intersect k[q,r]_q = k[q,r]
```

inside `k(q,r)`.  This proves the kernel assertion.

The two polynomial presentations also show that `pi_H` maps the two
charts surjectively onto `D(a)` and `D(q)` and is the translation
torsor there.  Their union is

```
D(a) union D(q) = A^2_(q,r) \ V(a,q)
                = A^2_(q,r) \ {(0,0)},
```

because at `q=0`, formula (2) reads `a=r^2/(2H)`.  This proves the
image and torsor assertions.

If a slice `s in A_H` existed, the slice theorem would give
`A_H=ker(D)[s]=k[q,r,s]`.  The morphism `(q,r)` would then be the
surjective projection `A^3 -> A^2`, contradicting the just-computed
missing origin.  Finally

```
ker(D on A_H[v])=(ker(D on A_H))[v],
```

and if `D(sum_i s_i v^i)=1`, comparison of the constant coefficient
would give `D(s_0)=1`.  Thus adjoining the invariant `v` cannot create
a slice.  This proves the lemma.

## Theorem (all nonconstant `phi` with `phi(0) != 0`)

Let

```
E = D + phi(h) partial_v
```

on `P[v]`, where `phi in k[T]` is nonconstant and `phi(0) != 0`.  Then
the action is proper and Zariski locally trivial, its geometric
quotient exists as a separated scheme, but that quotient is not
affine.  In particular `E` has no global slice.

First note that

```
h=q(qc-bd)+ad^2/2.
```

Writing `phi(T)=phi(0)+T psi(T)` therefore gives the explicit Bezout
identity

```
1 = phi(0)^(-1) phi(h)
    - phi(0)^(-1) psi(h) q(qc-bd)
    - phi(0)^(-1) psi(h) a d^2/2.            (5)
```

Thus the three invariant functions `a,q,phi(h)` generate the unit
ideal.  On their principal opens there are respectively the slices

```
b/a,                 d/q,                 v/phi(h).
```

The resulting translation charts give a Zariski locally trivial
geometric quotient.

There is also a direct properness check.  If `lambda` is the group
parameter and primes denote the translate of a point, then

```
b'-b=lambda a,
d'-d=lambda q,
v'-v=lambda phi(h).
```

Multiplying these three equalities by the Bezout coefficients in (5)
expresses `lambda` polynomially in the coordinates of the point and
its translate.  Hence the action graph morphism

```
Ga x A^5 -> A^5 x A^5
```

induces a surjection on coordinate rings and is a closed immersion.
It is therefore proper.  In particular the locally constructed
quotient is separated.

It remains to prove that the quotient is not affine.  Algebraic
closedness gives a root `H` of `phi`; the condition
`phi(0) != 0` makes `H != 0`.  The invariant ideal `(h-H)` is
`E`-stable, and on

```
P[v]/(h-H) = A_H[v]
```

the induced derivation is just the coefficientwise extension of `D`,
because `phi(H)=0`.  A putative equation `E(s)=1` would reduce to a
slice equation there, contrary to the lemma.

There is also a direct fiberwise proof of nonaffineness.  The invariant
`h` descends to a regular function on the geometric quotient `Y`, and
formation of the locally trivial torsor quotient commutes with the
base change `h=H`.  By the lemma and the fact that `v` is invariant on
this fiber, one gets

```
Y_H = (A^2_(q,r) \ {(0,0)}) x A^1_v.        (6)
```

This scheme is not affine.  Indeed its ring of global functions is
`k[q,r,v]` (the omitted line has codimension two in the normal affine
three-space), while its canonical morphism to the spectrum of that
ring misses the line `q=r=0`.  If `Y` were affine, the closed fiber
`Y_H` would be affine, contradicting (6).

Equivalently, one can finish from the no-slice statement: if the
geometric quotient `Y` were affine, the
locally trivial `Ga`-torsor would be classified by
`H^1(Y,O_Y)=0`, hence would be trivial.  A trivialization produces a
global fiber coordinate `s` with `E(s)=1`, which has just been ruled
out.
