# Stable rigidity of a smooth elliptic cubic cone in one variable

Throughout, `k` is algebraically closed of characteristic zero and

```
H in k[y_1,y_2,y_3]
```

is a homogeneous cubic whose zero locus `E=V_+(H) in P^2` is smooth.
Put `P=k[y_1,y_2,y_3]` and `R=P[x]`.

The purpose of this note is to remove the degree restriction from Section 7
of `cubic_frontier.md`.

## 1. Rigidity of the affine cone

**Lemma 1.** The affine cone

```
X=Spec(A),             A=P/(H),
```

admits no nontrivial `Ga`-action. Equivalently, `A` has no nonzero locally
nilpotent derivation.

**Proof.** The cone is smooth away from its vertex `o`: indeed, a nonzero
singular point would project to a singular point of `E`. The vertex is
singular because all first derivatives of the cubic vanish there. Hence `o`
is the unique singular point of `X`, and every `Ga`-action fixes it.

Blow up `o`. The resulting surface is the total space

```
pi:Y=Tot(O_E(-1)) -> E,
```

and the exceptional curve is its zero section. One way to see this
identification is to realize the blow-up as the closure of the graph of the
rational map `X -->> E`, `y |-> [y_1:y_2:y_3]`; on the chart over a standard
open subset of `E`, the remaining affine coordinate is the scalar along the
line represented by that point of `E`.

Because the center is invariant, the `Ga`-action lifts to `Y`, preserving the
exceptional curve. Moreover `pi` is invariant. In fact, for each point `z` of
`Y`, the composite of its orbit map with `pi` is a morphism

```
Ga=A^1 -> E.
```

Every such morphism is constant. It extends across infinity to a morphism
`P^1 -> E` (properness of `E`, or the valuative criterion on the missing
point), and a nonconstant morphism `P^1 -> E` is excluded by Riemann--Hurwitz:
in characteristic zero it would give

```
-2 = deg(phi)(2g(E)-2) + deg(Ramification) >= 0.
```

Pass now to the generic fibre of `pi`, over `K=k(E)`. It is `A^1_K`, and its
origin is fixed because the zero section is invariant. A locally nilpotent
derivation of `K[u]` is `c partial_u`; preservation of `(u)` forces `c=0`.
Thus the lifted action is trivial on the generic fibre. Since it is also over
`E`, it is trivial on a dense subset of `Y`, hence on `Y`, and therefore on
`X`. QED.

## 2. Rigidity before quotienting by `H`

The preceding quotient statement already implies the corresponding exact
statement in the polynomial ring.

**Lemma 2.** If `beta` is a locally nilpotent derivation of `P` and
`beta(H)=0`, then `beta=0`.

**Proof.** The induced locally nilpotent derivation on `A=P/(H)` vanishes by
Lemma 1. Hence

```
beta(y_i) in (H)                 for i=1,2,3.
```

If `beta` were nonzero, factor the largest common power of `H` from its three
coefficients:

```
beta=H^e gamma,
```

where at least one `gamma(y_i)` is not divisible by `H`. Since `beta(H)=0`
and `P` is a domain, `gamma(H)=0`. Also `gamma` is locally nilpotent. Indeed,
because `gamma(H)=0`,

```
beta^N(g)=H^(eN) gamma^N(g)
```

for every `g in P`; local nilpotence of `beta` and the fact that `H` is a
nonzerodivisor imply local nilpotence of `gamma`.

But `gamma` again induces zero on `A` by Lemma 1, so all `gamma(y_i)` are
divisible by `H`, contradicting maximality of `e`. QED.

## 3. One-variable stable rigidity

We use twice the following elementary fact.

**Invariant-principal-ideal fact.** If `partial` is an LND of a polynomial
domain and `partial(u) in (u)`, then `partial(u)=0`.

Indeed, `partial` preserves `(u)`, so

```
exp(t partial)(u)=u V(t).
```

Applying `exp(-t partial)` shows that `V(t)` is a unit in the polynomial ring
obtained by adjoining `t`. It is therefore a constant, and its value at
`t=0` is one. Differentiating at zero gives `partial(u)=0`.

**Theorem.** If `delta` is a locally nilpotent derivation of

```
R=k[y_1,y_2,y_3,x]
```

and `delta(H)=0`, then

```
delta(y_1)=delta(y_2)=delta(y_3)=0,
delta=a(y_1,y_2,y_3) partial_x
```

for a polynomial `a in P`.

**Proof.** Filter `R` by degree in `x`. For a coefficient of a `partial_y`
term, its filtration shift is its `x`-degree, while for the coefficient of
`partial_x` the shift is its `x`-degree minus one.

Suppose some `delta(y_i)` is nonzero. Set

```
r=max_i deg_x(delta(y_i)) >= 0,
s=deg_x(delta(x))-1,
M=max(r,s) >= 0,
```

where the degree of zero is `-infinity`. The top symbol `Delta` of `delta`
for this filtration is a nonzero LND homogeneous of filtration shift `M`.
For completeness, local nilpotence passes to the top symbol as follows: if
`Delta^N(in(g))` were nonzero for arbitrarily large `N`, it would be the top
symbol of `delta^N(g)`, contradicting local nilpotence of `delta`.

The possible top `partial_x` term has the form

```
Delta(x)=c(y) x^(M+1).
```

It belongs to `(x)`, so the invariant-principal-ideal fact gives
`Delta(x)=0`. Since `Delta` is nonzero, it follows that `M=r`; its remaining
part is

```
Delta=x^M beta,
```

where `beta` is a nonzero derivation of `P` and `beta(x)=0`. Since
`delta(H)=0`, its top symbol gives `Delta(H)=0`, hence `beta(H)=0`. Finally
`beta` is locally nilpotent: for `g in P`,

```
Delta^N(g)=x^(MN) beta^N(g),
```

and `Delta` is locally nilpotent. This contradicts Lemma 2. Thus every
`delta(y_i)` is zero.

It remains to determine `delta(x)`. After extending scalars from `P` to its
fraction field `K`, `delta` is an LND of `K[x]`. Every such derivation is
`c partial_x` with `c in K`: if `delta(x)` had positive `x`-degree, its
iterates on `x` would never vanish. Since originally `delta(x) in P[x]`, it
follows that `delta(x)=a(y) in P`. QED.

Thus `A=P/(H)` is not only rigid: its one-variable polynomial extension has

```
ML(A[x])=A.
```

Here are the details, since stable rigidity does not follow formally from
rigidity. The singular locus of `X times A^1` is the intrinsic reduced line
`{o} times A^1`, so every `Ga`-action preserves it and lifts to its blow-up

```
Tot(O_E(-1)) times A^1 -> E.
```

As in Lemma 1, every orbit has constant image in `E`. On the generic fibre
over `k(E)` we have an LND of `k(E)[u,x]` preserving the exceptional divisor
`u=0`. The invariant-principal-ideal fact gives `partial(u)=0`. The rational
functions `y_i/y_j` come from the base `E`, and each `y_i` is locally `u`
times a base section; hence all the `y_i` are fixed. Thus every LND of `A[x]`
kills `A`. Conversely, `partial_x` has kernel exactly `A`, proving the stated
equality of Makar--Limanov invariants. The filtration proof above gives the
stronger lifting statement for LNDs of `P[x]` which preserve the actual
polynomial `H`.

## 4. Consequence for the cubic leading field

Let `f=f_3+f_2+f_1+f_0 in R` have

```
f_3=H(y_1,y_2,y_3),
```

and let `D=D_0+...+D_d` be an LND with `D(f)=1`, decomposed by ordinary
coefficient degree. Its top homogeneous part `delta=D_d` is an LND and the
highest degree equation is `delta(H)=0`. The theorem therefore gives

```
D_d=q(y_1,y_2,y_3) partial_x,
```

with `q` homogeneous of degree `d`. This holds for every `d`, not merely
`d<=2`.

The next exact equation is

```
q partial_x(f_2) + D_(d-1)(H)=0.                 (*)
```

This equation alone does not justify deleting `D_d`: the difference of two
LNDs need not be locally nilpotent, and `D_(d-1)` itself need not be an LND.
Modulo the Jacobian complete intersection

```
J=(H_1,H_2,H_3) in P,
```

equation `(*)` gives the necessary divisibility condition

```
q partial_x(f_2)=0 in (P/J)[x].
```

Writing `partial_x(f_2)=alpha x+L(y)`, this says

```
q(alpha x+L)=0 mod J.
```

For degrees `d>=4` this condition can be vacuous because the Artinian
complete intersection `P/J` has socle degree three. Thus a descent from the
top field requires genuinely using local nilpotence across the lower
homogeneous pieces, not merely the first two degree equations. No such
descent is asserted here.

## 5. A rigorous degree-lowering mechanism when the base is stable

There is one useful situation in which the vertical leading term really can
be removed. It is important that this is an additional hypothesis on the
whole derivation, not a consequence of the top equation.

**Lemma.** Let `P=k[y_1,y_2,y_3]`, let `D` be an LND of `P[x]`, and suppose
`D(P) subset P`. Write `theta=D|_P`. Then

```
D=theta+b(y) partial_x
```

for some `b in P`. If `D` has a slice and

```
b in k+theta(P),
```

then every slice of `D` is a coordinate of `P[x]`.

**Proof.** The exponential `Phi_t=exp(tD)` preserves `P[t]`. An automorphism
of the one-variable polynomial ring `P[t][x]` which preserves its coefficient
ring sends `x` to `a x+c`, with `a in P[t]^*`. Here `P[t]^*=k^*`, and
specializing at `t=0` gives `a=1`. Differentiation at zero therefore gives
`D(x)=b(y)`.

Choose `g in P` and `c in k` with `b=c+theta(g)`, and make the shear

```
x'=x-g.
```

Then `D(x')=c`. If `c!=0`, the literal polynomial coordinate `x'/c` is a
slice. The slice theorem gives

```
P[x]=ker(D)[x'],
ker(D) isomorphic to P[x]/(x')=k^[3].
```

Any other slice differs from `x'/c` by an invariant, so it too is a
coordinate after choosing polynomial generators of `ker(D)`.

If `c=0`, the new variable `x'` is invariant. Expand a given slice `s` as a
polynomial in `x'`. Since `D(s)=1` and `D` acts coefficientwise by `theta`,
the constant coefficient of `s` is a slice for `theta` on `P`. Hence
`P=ker(theta)[s_0]`. Cancellation in dimension two gives
`ker(theta)=k^[2]`, so `s_0` is a coordinate of `P`. Applying the slice
theorem to `D` now gives

```
ker(D) isomorphic to P[x]/(s_0)=k^[3],
```

and again every slice of `D` is a coordinate. QED.

In particular, if the highest homogeneous part of `b` is an actual highest
homogeneous part of `theta(g)`, the shear `x -> x-g` lowers that vertical
coefficient degree. What remains missing in the unrestricted cubic problem
is a reason why repeated lowering must put `b` in `k+theta(P)`, or even a
reason why the full slice derivation must stabilize `P`. The theorem of
Section 3 classifies only its highest homogeneous field and does not provide
either assertion.
