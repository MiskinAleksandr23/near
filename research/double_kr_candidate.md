# The doubled Koras--Russell candidate

Let `k` be a field of characteristic zero and put

```text
g=z^2+t^3,
F=a^2 b^2 y+g+a,
A=k[a,b,y,z,t]/(F).
```

Also let

```text
R=k[a,Y,z,t]/(a^2 Y+g+a),
```

the coordinate ring of the Russell cubic, with `Y` deliberately
distinguished from the variable `y` of `A`.  All tensor products and
differentials below are over `k`.

The ring `A` is a domain.  Indeed, in `k[a,b,z,t][y]` the polynomial
`F` is linear in `y`, and its two coefficients `a^2b^2` and `a+g` are
coprime: neither `a` nor `b` divides `a+g`.  Thus `F` is primitive and
irreducible.

The purpose of this note is not to assert that `A[u]` is or is not a
polynomial ring.  It records three exact calculations: the cotangent and
standard cohomological invariants, the affine-modification presentation,
and the precise hyperplane-polynomial consequence of a hypothetical
isomorphism `A[u] ~= k^[5]`.

## 1. Smoothness and an explicit free cotangent bundle

The partial derivatives of `F` are

```text
p:=F_a=1+2ab^2y,       q:=F_b=2a^2by,
F_y=a^2b^2,            F_z=2z,             F_t=3t^2.
```

The hypersurface is smooth.  Indeed, a common zero of `F_y,F_z,F_t`
would satisfy `ab=0` and `z=t=0`.  If `a=0`, then `F_a=1`.  If `b=0`
and `a!=0`, then `F=a!=0`, so the point does not lie on the
hypersurface.  This argument remains valid after every field extension.

Define

```text
r=1-2ab^2y,            s=2b^3y.
```

There is the following Bezout identity entirely inside `A`:

```text
rp+sq
 = (1-2ab^2y)(1+2ab^2y)+(2b^3y)(2a^2by)
 = 1.                                                     (1)
```

Consider the five columns in `A^5`, written in the ordered basis
`da,db,dy,dz,dt`,

```text
v=(p,q,F_y,F_z,F_t)^t,
w=(-s,r,0,0,0)^t,
e_y=(0,0,1,0,0)^t,
e_z=(0,0,0,1,0)^t,
e_t=(0,0,0,0,1)^t.
```

The determinant of the matrix with these columns is

```text
det[v w e_y e_z e_t] = pr+qs = 1                       (2)
```

by (1).  Thus these columns form an `A`-basis of `A^5`.

The conormal sequence for the smooth hypersurface is

```text
0 -> A dF -> A da + A db + A dy + A dz + A dt
  -> Omega^1_A -> 0.
```

Under the coefficient-vector identification, `dF` is precisely `v`.
Quotienting the basis (2) by `A v` proves:

**Lemma 1.**  The module `Omega^1_A` is free of rank four, with explicit
basis

```text
omega=-2b^3y da+(1-2ab^2y)db,   dy, dz, dt.             (3)
```

In particular,

```text
Omega^j_A ~= A^(binom(4,j)),
Omega^1_{A[u]} ~= (A[u])^5,
Omega^j_{A[u]} ~= (A[u])^(binom(5,j)).                  (4)
```

For completeness, the basis of the tangent module dual to (3) can be
written without solving any equations.  In the ambient polynomial ring
notation put

```text
D_0 = -q partial_a+p partial_b,
D_y = partial_y-F_y(r partial_a+s partial_b),
D_z = partial_z-F_z(r partial_a+s partial_b),
D_t = partial_t-F_t(r partial_a+s partial_b).
```

Identity (1) gives `D_i(F)=0`, so the four derivations descend to `A`,
and direct evaluation on (3) shows that they are the dual basis.

### Hochschild and de Rham consequences

Since `A` and `A[u]` are smooth over a characteristic-zero field, HKR
applies.  In particular,

```text
HH_j(A/k) ~= Omega^j_A ~= A^(binom(4,j)),
HH^j(A,A) ~= wedge^j Der_k(A) ~= A^(binom(4,j)),         (5)
```

and the analogous groups for `A[u]` have ranks `binom(5,j)`.  These are
isomorphisms of modules; (5) does not identify the Hochschild products or
the de Rham differential with those of a polynomial ring.  Nevertheless,
it proves that neither the cotangent module, the canonical module, nor the
underlying HKR modules obstruct `A[u] ~= k^[5]`.

If `HD` is intended as Hodge cohomology rather than de Rham cohomology,
affineness and (4) give the complete calculation

```text
H^q(Spec A,Omega^p)=0                         for q>0,
H^0(Spec A,Omega^p)=A^(binom(4,p)),
H^0(Spec A[u],Omega^p)=A[u]^(binom(5,p)).                (5a)
```

If `HD^*` denotes algebraic de Rham cohomology, the answer is also the
same as for affine space.  This member is the variety
`X_1((2,2),1)` in the higher Koras--Russell family and is known to be
`A^1`-contractible.  Algebraic de Rham cohomology is `A^1`-homotopy
invariant for smooth characteristic-zero schemes, hence

```text
H^0_dR(A/k)=k,       H^i_dR(A/k)=0 for i>0,              (6)
H^*_dR(A[u]/k)=H^*_dR(A/k).                              (7)
```

Here (6) uses the cited `A^1`-contractibility theorem; it is not being
deduced merely from freeness of (3).  Via the characteristic-zero
de Rham--cyclic comparison it also gives `HP_even(A)=k`,
`HP_odd(A)=0`, and the same answer after adjoining `u`.

## 2. Two affine-modification presentations, with signs

**Lemma 2.**  The ring `A` is simultaneously the affine modification
`R[b][(b^2,Y)/b^2]` and the affine modification
`D[(a^2b^2,a+g)/(a^2b^2)]`; in the second description the adjoined
fraction `(a+g)/(a^2b^2)` corresponds to `-y`.

First set `C=R[b]` and `I=(b^2,Y) subset C`.  The affine-modification
algebra is the subalgebra

```text
C[I/b^2]=C[Y/b^2] subset C_b.
```

It has a presentation which involves no division:

```text
C[I/b^2]
 ~= k[a,b,Y,y,z,t]/(a^2Y+g+a, b^2y-Y).
```

Eliminating `Y` by the second equation gives

```text
C[I/b^2] ~= k[a,b,y,z,t]/(a^2b^2y+g+a)=A.               (8)
```

Thus the map in (8) is exactly `Y |-> b^2y`; there is no sign change in
this presentation.

There is also a presentation as a modification of affine four-space.
Let

```text
D=k[a,b,z,t],     f=a^2b^2,     J=(f,a+g).
```

Then

```text
D[J/f]=D[(a+g)/f] subset D_f.
```

Writing `T=(a+g)/f`, it has the division-free presentation

```text
D[J/f] ~= D[T]/(fT-(a+g)).                               (9)
```

The isomorphism from (9) to `A` sends

```text
T |-> -y,
```

because `f(-y)-(a+g)=-(a^2b^2y+a+g)=0`; its inverse sends
`y |-> -T`.  Therefore

```text
A ~= D[(a+g)/(a^2b^2)],
```

with the important convention `(a+g)/(a^2b^2)=-y`.  This checks the
sign without dividing by `a` or by `b` in either ring map.

Geometrically, the center in the nonreduced divisor `V(a^2b^2)` has two
different reduced pieces:

```text
a=0:  V(a,g),       the cuspidal curve times A^1_b;
b=0:  V(b,a+g),     an affine plane with coordinates z,t.
```

The exceptional divisor over the second piece is

```text
A/(b) ~= k[a,y,z,t]/(a+g) ~= k[y,z,t]=k^[3].            (10)
```

Adjoining `u` to (8) or (9) gives the cylinder modification, with `u`
passive; it does not turn either displayed fraction into an allowed
division along `a=0` or `b=0`.

## 3. The smooth hyperplane-polynomial obstruction

The fibers of the regular function `b` on `Spec(A[u])` are explicit.
At zero, (10) gives

```text
A[u]/(b) ~= k[y,z,t,u]=k^[4].                            (11)
```

For `c in k*`, define

```text
theta_c:R[u] -> A[u]/(b-c),
a |-> a,  z |-> z,  t |-> t,  u |-> u,  Y |-> c^2y.
```

It is an isomorphism: the defining relation of `R` maps to
`a^2c^2y+g+a`, and its inverse sends `y` to `c^(-2)Y`.  Therefore

```text
A[u]/(b-c) ~= R[u]                     for every c!=0.  (12)
```

The morphism

```text
b:Spec(A[u]) -> A^1
```

is smooth.  Indeed, `A[u]` is a domain and hence torsion-free, thus flat,
over the PID `k[b]`.  The zero fiber is the affine four-space (11), while
every nonzero geometric fiber is the product of the smooth Russell cubic
with an affine line by (12); the generic geometric fiber has the same
description after replacing `c` by the invertible generic value of `b`.
Flatness, finite presentation, and geometric regularity of all fibers give
smoothness.

Now suppose that an isomorphism

```text
Phi:A[u] ~-> P=k[U_1,...,U_5]
```

exists, and put `h=Phi(b)`.  Transporting (11)--(12) gives:

**Lemma 3.**  The polynomial `h` defines a smooth morphism
`h:A^5 -> A^1` such that

```text
P/(h)   ~= k^[4],
P/(h-c) ~= R[u]             for every c in k*,           (13)
P_h     ~= R[u][b,b^(-1)].                                (14)
```

Formula (14) follows already before applying `Phi`, because the first
modification presentation becomes trivial after inverting `b`:

```text
A_b ~= R[b,b^(-1)],       Y <-> b^2y.
```

If `h` is a coordinate of `P`, then every quotient `P/(h-c)` is a
four-variable polynomial ring.  Taking any `c!=0` in (13) proves

```text
R[u] ~= k^[4].                                           (15)
```

Consequently a hypothetical trivialization of this cylinder has a sharp
algebraic alternative:

1. the cylinder over the Russell cubic is affine four-space, as in (15);
   or
2. `h` is a non-coordinate smooth polynomial in five variables even though
   its zero fiber is `A^4`.

The second branch is precisely a hyperplane/epimorphism obstruction of
Abhyankar--Sathaye type.  Thus an isomorphism `A[u] ~= k^[5]` cannot arise
from a coordinate-trivialization of the visible function `b` without at
the same time trivializing the Russell cylinder.

There is a useful finite-degree strengthening.  Smoothness of `h` implies
that its five first partial derivatives generate the unit ideal.  If
`deg(h)<=2`, write

```text
h(x)=1/2 x^t Qx+l^t x+c
```

with `Q` symmetric.  The affine linear system `Qx+l=0` has no solution,
so elementary linear algebra gives a row `lambda` with

```text
lambda^t Q=0,       lambda^t l!=0.
```

The constant vector field `partial_lambda` then satisfies
`partial_lambda(h)=lambda^t l in k*`, and an affine linear change writes
`h` as one variable plus a polynomial in the other four.  Hence `h` is a
coordinate.  We have proved the checkable conditional implication

```text
A[u] ~= k^[5] and deg(Phi(b))<=2  ==>  R[u] ~= k^[4].    (15a)
```

The same conclusion holds whenever `Phi(b)` has a nonzero constant
directional derivative.  It also holds for the verified cubic class in
which the leading cubic form is a nonzero cube of a linear form: the
unimodular-gradient cubic argument then produces such a constant
direction.  Thus, unless the Russell cylinder is affine four-space, every
hypothetical image of `b` is forced outside these low-degree and
rank-one-at-infinity classes.

## 4. Why local and specialization tests do not strengthen Lemma 3

The family is algebraically trivial over the punctured base but formally
trivial along the special fiber.  Both assertions admit explicit formulas.

The punctured statement is the already used isomorphism

```text
A[u]_b ~-> R[u][b,b^(-1)],       Y |-> b^2y,             (16)
```

whose inverse sends `y` to `b^(-2)Y`.  Division is legitimate in (16)
because this is an isomorphism only after localizing at `b`.

For the formal statement, let

```text
C(q)=sum_(n>=0) Cat_n q^n in Z[[q]]
```

be the Catalan series, characterized uniquely by

```text
C(q)=1+q C(q)^2.
```

In `k[y,z,t,u][[b]]` put

```text
alpha=-g C(b^2yg).                                      (17)
```

Then

```text
alpha+g+b^2y alpha^2
 = g(1-C(b^2yg))+b^2yg^2 C(b^2yg)^2
 = 0.                                                    (18)
```

Consequently there is a continuous homomorphism

```text
widehat(A[u])_(b) -> k[y,z,t,u][[b]]
```

sending `a` to `alpha` and fixing `b,y,z,t,u`.  It is an isomorphism.
One direct proof, avoiding a formal implicit-function theorem, works
modulo every `b^N`.  The truncation of (17) supplies a solution of (18)
modulo `b^N`.  Any two solutions congruent to `-g` modulo `b` have
difference `delta` satisfying

```text
delta (1+b^2y(alpha_1+alpha_2))=0.
```

The second factor is a unit modulo `b^N`, so `delta=0`.  Since the class
of `a` in `A[u]/(b^N)` is such a solution, the mutually inverse maps give

```text
A[u]/(b^N) ~= k[y,z,t,u,b]/(b^N)       for every N>=1,   (19)
widehat(A[u])_(b) ~= k[y,z,t,u][[b]].                    (20)
```

Thus every infinitesimal deformation class and every invariant of the
formal neighborhood of `b=0` is already the one of a coordinate
hyperplane.  Any obstruction must see the global gluing between (16) and
(20), not merely the special fiber or its infinitesimal thickenings.

The visible formal trivialization cannot be algebraized, even rationally,
over the chosen four-dimensional fiber coordinates.  Set

```text
B_0=k[b,y,z,t,u],       K=Frac(B_0).
```

Viewed as an equation for `a`, the relation is

```text
b^2y a^2+a+g=0,
```

with discriminant

```text
Delta=1-4b^2yg.                                         (20a)
```

The element `Delta` is not a square in `K`: regarding it as a degree-one
polynomial in `y` over `k(b,z,t,u)`, its irreducible divisor occurs with
valuation one, whereas every square has even valuation.  Hence the
quadratic in `a` has no root in `K`.  In particular, there is no
polynomial `alpha in B_0` satisfying the relation.  The latter also has
the elementary degree proof that, if `d=deg_y(alpha)`, then
`b^2y alpha^2` has degree `2d+1`, strictly larger than the degrees of
`alpha` and `g`, so its leading term cannot cancel.

Thus (17) is genuinely a Henselian/formal branch of a generically
quadratic projection; it is not the expansion of a rational coordinate
elimination.  Concretely, on `A` one has
`(1+2b^2ya)^2=Delta`; the completion selects the square root congruent to
`1` modulo `b`, although `Delta` has no square root in `K`.  This is the
exact obstruction to the most direct attempt
to turn (20) into a global cylinder trivialization.  It does not exclude
a trivialization using a different set of five global coordinates.

There is nevertheless an explicit etale chart on a Zariski neighborhood
of the whole special fiber.  Recall `p=1+2ab^2y` and introduce `lambda`.
The identity just proved gives an isomorphism

```text
A[u]_(p(1+p))
 ~= B_0[lambda,1/(lambda(1+lambda))]/(lambda^2-Delta),   (20c)
```

where the map from the right-hand side to the left-hand side sends
`lambda` to `p`, and its inverse sends

```text
a |-> -2g/(1+lambda).
```

Indeed, the latter element satisfies `b^2ya^2+a+g=0`, and
`1+2b^2ya=lambda` follows from `lambda^2=1-4b^2yg`.
The right side is etale over `B_0` because `2lambda` is invertible.  The
open set on the left contains all of `b=0`, where `p=1`, and (20c)
restricts to the identity chart of the special affine four-space.  Thus
the family is even etale-standard in the total-space direction near its
special fiber.  This is distinct from an etale *base change* on `A^1_b`;
the quadratic cover depends on the fiber variables through `Delta`.

There is also no ordinary Makar--Limanov specialization signal after the
single stabilization.  The zero fiber in (11) has ML invariant `k`, and
the theorem on the Russell cylinder gives

```text
ML(R[u])=k,
```

so every geometric fiber of `b` has the same trivial ML invariant.
Before adjoining `u`, the nonzero fiber has `ML(R)=k[a]`; the added
variable is exactly what destroys this distinction.

One can make the statement relative to the visible base completely
precise.  Let `ML_(k[b])` be the intersection of the kernels of all
locally nilpotent `k[b]`-derivations, and let `DK_(k[b])` be the algebra
generated by the kernels of the nonzero such derivations.  Then

```text
ML_(k[b])(A[u])=k[b],       DK_(k[b])(A[u])=A[u].        (20b)
```

For the ML equality, the inclusion from right to left is tautological.
After tensoring with `K=k(b)`, (16) identifies the generic fiber with
`R_K[u]`, whose ML invariant is `K`.  Every locally nilpotent
`K`-derivation of the generic fiber can be multiplied by a sufficiently
large power of `b` so that it preserves the finitely many generators of
`A[u]`; the multiplier lies in its kernel, so the resulting derivation is
still locally nilpotent and is a `k[b]`-derivation.  Hence an element of
the relative ML invariant lies in

```text
A[u] intersect k(b)=k[b].
```

To justify the last equality, write an element of the intersection as a
coprime fraction `p(b)/q(b)`.  Every irreducible factor of `q` remains
prime in `A[u]`: quotienting by it is the same defining hypersurface over
the finite residue-field extension and is a domain by the primitive
linear-in-`y` argument used at the start of the note.  Regularity of the
fraction would force that factor to divide `p`, a contradiction.

For the relative Derksen equality, `partial_u` is a nonzero
`k[b]`-LND with kernel `A`, while

```text
delta_z(z)=a^2b^2,   delta_z(y)=-2z,
delta_z(a)=delta_z(b)=delta_z(t)=delta_z(u)=0
```

is another nonzero `k[b]`-LND of `A[u]` and its kernel contains `u`.
Their kernels generate `A[u]`.  Thus even the relative ML/Derksen pair is
exactly `(k[b],A[u])`, the same formal pattern as for a polynomial ring
over `k[b]`.

These facts isolate the hypotheses missing from standard fibration
theorems:

* If `Spec(A[u]) -> A^1_b` were Zariski locally trivial on a neighborhood
  of zero with fiber `A^4`, then a nonzero fiber in that neighborhood and
  (12) would give `R[u] ~= k^[4]`.
* The same conclusion holds for geometric fibers if the family becomes
  trivial after an etale base neighborhood of zero.
* The usual affine-space-fibration or residual-coordinate theorems require
  the general fibers themselves to be affine spaces.  In this family that
  missing hypothesis is exactly the assertion `R[u] ~= k^[4]`; smoothness,
  `A^1`-contractibility, formal triviality, and trivial fiberwise ML do not
  replace it.

Thus local-triviality machinery does not independently eliminate branch
2 of Lemma 3.  Proving the required local triviality would already settle
the Russell-cylinder subproblem.

## 5. A motivic check

Even the elementary Grothendieck class is that of affine space.  Let
`L=[A^1]`.  On the Russell cubic, the locus `a!=0` is
`G_m times A^2`, while at `a=0` it is `A^1_Y` times the cusp
`z^2+t^3=0`.  The cusp minus its origin is `G_m` via

```text
lambda |-> (z,t)=(lambda^3,-lambda^2),
```

with inverse `lambda=-z/t`; hence its class is `L`.  Therefore

```text
[Spec R]=(L-1)L^2+L^2=L^3.
```

Using (16) away from `b=0` and (10) at `b=0` gives

```text
[Spec A]=(L-1)[Spec R]+L^3=L^4,
[Spec A[u]]=L^5.                                        (21)
```

So the boundary decomposition visible in the affine modification also
produces no obstruction in the Grothendieck ring.
