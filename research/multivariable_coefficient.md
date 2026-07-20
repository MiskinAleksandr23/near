# A multivariable coefficient: a conditional rational SNC theorem

Throughout, `k` is algebraically closed of characteristic zero,

```
R = k[x,u,v,w],
f = a(u,v)x + G(u,v,w),
R = B[f].
```

Write

```
a = lambda product_(i=1)^r p_i^(m_i),   m_i >= 1,
D_i = V(p_i) subset A2_(u,v),
D = V(a)_red.
```

The purpose of this note is to isolate a genuinely multivariable class in
which cancellation can still be proved.  Multiplicities of the factors of
`a` play no role in the conclusion.

## The theorem

**Theorem.** Suppose that:

1. every `D_i` is smooth and isomorphic to `A1`;
2. the reduced divisor `D` has only ordinary double points (distinct
   components meet transversely, and no three components meet);
3. at every node `s of D`, the polynomial `G(s,w)` is nonconstant.

Then `B=k^[3]` and `f` is a coordinate of `R`.

For `r=1`, condition (1) and Abhyankar--Moh--Suzuki make `p_1` a plane
coordinate, and the univariate-coefficient theorem applies.  More
generally, the same is true whenever the incidence graph is disconnected:

**Parallel-components lemma.** A finite collection of embedded affine
lines in `A2` whose incidence graph is disconnected is in fact a
collection of parallel coordinate lines.

Indeed, rectify one member `D_1` to `u=0`.  Any component `C` in a
different graph component is disjoint from `D_1`; hence `u|_C` is a
nowhere-vanishing regular function on `C=A1`, and is a constant `c!=0`.
Thus `C` is the whole line `u=c`.  If a component `D_j` met `D_1`, then
`u|_(D_j)` would be a nonconstant polynomial having the value zero, hence
would also have the value `c`; this would make `D_j` meet `C`, a
contradiction.  Therefore no component meets `D_1`, and repeating the
argument shows that all components are the parallel lines `u=c_i`.

It follows that in the disconnected case

```
a=lambda product_i (u-c_i)^(m_i)
```

after a plane automorphism, so the univariate-coefficient theorem applies.
The proof below treats the genuinely new case in which the graph is
connected and `r>=2`.  The first new coefficient divisor is

```
a(u,v)=u^m v^n
```

for completely arbitrary positive `m,n`, provided the single node
restriction `G(0,0,w)` is nonconstant.

## 1. Factoriality at a generic level

For every `c in k`, put

```
X_c = Spec R/(f-c).
```

Translation in the polynomial variable of `B[f]` identifies every
`R/(f-c)` with `B`.  Hence every `X_c` is a smooth factorial threefold,
has only constant units, and has compactly supported Euler characteristic
one.

Let `t_i` be a coordinate on `D_i=A1`, and denote the restriction of `G`
to `D_i x A1_w` by

```
g_i(t_i,w).
```

**Generic divisor lemma.** If `c` is different from the constant value of
`G(s,w)` at every node where that restriction is constant, then, for every
`i`, `g_i-c` is nonconstant, irreducible, and squarefree in `k[t_i,w]`.

Under hypothesis (3), the exceptional set in this statement is empty, but
the qualified formulation records exactly where the valuation argument can
fail in the more general problem.

**Proof.** If `g_i-c=0`, then `p_i` divides `f-c`, contrary to the fact
that `R/(f-c)` is a domain.  If `g_i-c` is a nonzero constant, then `p_i`
is a unit on `X_c`, contrary to `B^*=k^*` (the map `k[u,v]->R/(f-c)` is
injective by comparison of degrees in `x`).

Factor

```
g_i-c = d product_j q_j^(e_j).
```

The ideals `P_j=(p_i,q_j)` in `R/(f-c)` are height-one primes.  At the
generic point of `q_j`, reduction modulo `p_i` gives

```
ord_(P_j)(p_i)=e_j.                                  (1)
```

Factoriality gives `P_j=(h_j)`.  After inverting `a`, one can eliminate
`x`, so

```
(R/(f-c))_a = k[u,v,a^(-1),w].
```

The units of the ring on the right are precisely

```
k^* product_l p_l^Z.
```

Thus in the common fraction field

```
h_j = epsilon product_l p_l^(n_l).
```

By the choice of `c`, no `P_j` contains another component equation `p_l`:
such containment could occur only at a node `s` where `G(s,w)=c`
identically.  Taking valuations at all the `P_j'` over `p_i` and using (1)
therefore gives

```
delta_(j,j') = n_i e_(j')   for every j'.
```

This forces exactly one factor and exponent one.  QED.

Notice that the powers `m_i` in `a` never enter this calculation: it is
the Cartier divisor of the reduced equation `p_i` that is being measured.

## 2. The Euler identity on the coefficient divisor

Let

```
Y_c = V(D,G-c) subset D x A1_w.
```

Over `A2-D`, the equation `f=c` eliminates `x`.  Over `D`, the `x`
coordinate is free and the remaining equation is `G=c`.  Additivity of
Euler characteristic therefore gives

```
1 = chi_c(X_c)
  = chi_c(A2-D) + chi_c(Y_c)
  = 1-chi_c(D) + chi_c(Y_c),
```

and hence, for every `c`,

```
chi_c(Y_c)=chi_c(D).                                 (2)
```

Let the incidence multigraph have `r` vertices and `e` edges, one edge
for every intersection point of two components.  The SNC hypotheses give

```
chi_c(D)=r-e.                                        (3)
```

For an edge `s in D_i intersect D_j`, set

```
h_s(w)=G(s,w).
```

### Generic equality is termwise sharp

Choose `c` simultaneously outside the critical values of the finitely many
maps `g_i:A2->A1` and of all the one-variable polynomials `h_s`.  The
generic divisor lemma says that

```
C_i,c=V(g_i-c)
```

is an irreducible smooth affine curve.  Therefore

```
chi_c(C_i,c) <= 1.                                   (5)
```

If `d_s=deg h_s`, then the two components meeting at the edge `s` meet in
exactly `d_s` points inside `Y_c`.  There are no triple intersections, so
(2)-(3) become

```
r-e = sum_i chi_c(C_i,c) - sum_s d_s.                (6)
```

There are `e` summands in the last sum, each at least one.  Combining (5)
and (6) gives a chain

```
r-e <= r-sum_s d_s <= r-e.
```

Both inequalities are equalities.  Consequently

```
chi_c(C_i,c)=1 for every i,    d_s=1 for every edge s. (7)
```

An irreducible smooth affine curve has Euler characteristic at most one,
with equality only for `A1`.  Hence every generic `C_i,c` is `A1`, and the
Abhyankar--Moh--Suzuki theorem says that `g_i-c`, equivalently `g_i`, is a
coordinate of `k[t_i,w]`.

## 3. A plane-coordinate compatibility lemma

We use the following elementary consequence of plane rectifiability.

**Lemma.** Let `g in k[t,w]` be a coordinate.  If

```
g(0,w)=alpha w+beta,   alpha!=0,
```

then `(t,g)` is a coordinate pair.  In particular,

```
g=mu w+P(t),   mu in k^*.
```

**Proof.** Choose a companion `h` with `k[t,w]=k[g,h]`.  On the line
`t=0`, the function `g` itself generates `k[w]`; hence in the `(g,h)`
plane this line is the graph `h=Q(g)`.  Its principal ideal is both `(t)`
and `(h-Q(g))`, up to a nonzero scalar.  Therefore
`k[t,g]=k[g,h]=k[t,w]`.  An automorphism of the one-variable polynomial
ring `k[t][w]` is affine in `w`, proving the last assertion.  QED.

Every vertex of the connected graph has an incident edge.  By (7), at
that edge `g_i(t_i(s),w)` has degree one.  After translating `t_i`, the
lemma gives

```
g_i(t_i,w)=alpha_i w+P_i(t_i),   alpha_i in k^*.     (8)
```

At an intersection, equality of the two restrictions shows that adjacent
`alpha_i` agree (although only their nonvanishing is needed below).

Thus, at every point `z in D`,

```
G(z,w) is a degree-one polynomial in w.              (9)
```

## 4. The quotient is a trivial smooth A1-fibration

Identify

```
B = k[u,v,x,w]/(a x+G).
```

Consider `Spec(B)->A2_(u,v)`.  Its geometric fiber at a point `z` is:

* `A1_w` if `a(z)!=0`, by eliminating `x`;
* `A1_x` if `a(z)=0`, by (9), which eliminates `w`.

Thus every geometric fiber is `A1`.  The total space is regular (because
`B[f]=R`), hence Cohen--Macaulay; the base is regular; and all fibers have
pure dimension one.  Miracle flatness makes the morphism flat.  It is then
smooth, since all geometric fibers are smooth.

The affine-line fibration theorem of Kambayashi--Miyanishi (the `n=1`
case of the Dolgachev--Weisfeiler problem) makes an affine faithfully flat
finite-type morphism over a locally factorial integral base, with every
fiber an affine line, a Zariski locally trivial affine-line bundle.  Thus
its transition functions lie in `Aff_1=G_a semidirect G_m`.  On `A2`, both
the line-bundle class and the corresponding additive torsor class vanish:

```
Pic(A2)=0,    H^1(A2,O)=0.
```

Consequently the fibration is trivial and

```
B = k[u,v]^[1] = k^[3].
```

Finally `R=B[f]`, so a polynomial basis of `B` together with `f` is a
polynomial basis of `R`: `f` is an ambient coordinate.  QED.

## 5. Exact frontier of this argument

The proof uses the following three pieces, each in an essential place.

* UFD at all translates makes every generic curve `g_i=c` integral and
  reduced, provided the chosen level is not identically attained at a
  node.
* Rational SNC components make `chi(D)=#vertices-#edges`, while every
  generic integral curve over a component has Euler characteristic at most
  one.
* Nonconstant node restrictions ensure that the height-one primes over
  different `p_i` do not merge at the chosen generic level.  The
  parallel-components lemma sends the disconnected case back to the
  univariate theorem.

For a component `D_i` of positive genus or with several places at infinity,
the numerical upper bound `chi(C_i,c)<=1` is no longer sharp against
`chi(D_i)`.  The equality

```
chi(Y_c)=chi(D)
```

then permits genuine negative Euler contributions and does not force
`C_i,c=A1`.  This is the exact geometric failure of the present mechanism,
not a counterexample to cancellation.

There is a second, independent frontier: if `G(s,w)=gamma` at a node, then
at the special level `c=gamma` the prime `(p_i,p_j)` can be height one in
`R/(f-c)` and lie simultaneously in the divisors of `p_i` and `p_j`.
The valuation equation then has cross-terms

```
ord_P(h)=n_i ord_P(p_i)+n_j ord_P(p_j),
```

so the one-component delta equation used in the generic divisor lemma is
invalid.  For example, with `a=uv` and

```
G=u+v(vw+1),
```

the restriction `G(0,v,w)=v(vw+1)` is reducible at the constant node level
zero.  (The resulting polynomial is nevertheless a coordinate: after
`U=u+v` and `z=w-x` it becomes
`U+v(Ux+vz)`, which is the image of `U` under the exponential automorphism
associated with the locally nilpotent derivation
`v partial_U-x partial_z` and invariant `Ux+vz`.)

Thus constant-node levels require a coupled valuation analysis, not the
false assertion that each branch divisor remains irreducible there.  The
theorem above deliberately assumes them away.

## 6. Exact reduction at one constant node (`a=uv`)

There is nevertheless a fairly rigid statement in the first omitted case.
Assume `D=V(uv)` and

```
G(0,0,w)=gamma.
```

Write

```
g_u(v,w)=G(0,v,w),   g_v(u,w)=G(u,0,w).
```

At a generic level `c!=gamma`, the generic divisor lemma applies and the
two curves `g_u=c`, `g_v=c` are smooth and irreducible.  Their intersection
at the node is empty, while the Euler identity is

```
chi(g_u=c)+chi(g_v=c)=1.
```

Each summand is at most one, so, after interchanging `u,v`, their types are
exactly

```
g_v=c : A1,        g_u=c : G_m.                       (10)
```

The first polynomial is a plane coordinate by Abhyankar--Moh--Suzuki.
Since `g_v-gamma` vanishes on the whole line `u=0`, its irreducibility as a
coordinate polynomial forces

```
g_v(u,w)=gamma+lambda u,   lambda in k^*.            (11)
```

The special level can now be analyzed by the *coupled* divisor matrix.
For `A=R/(f-gamma)`, the localization sequence for the UFD `A` and

```
A_(uv)=k[u,v,(uv)^(-1),w]
```

identifies the lattice generated by `u,v` with the free lattice on all
height-one boundary primes.  In particular, there are exactly two such
primes and their valuation matrix is unimodular.

Factor on the other branch

```
g_u-gamma=v^e product_j H_j^(d_j),   e>=1,
```

with no `H_j` associated to `v`.  The shared node divisor is the only
component of `div(v)`, with coefficient one by (11).  Hence the boundary
prime count forces exactly one `H`, and unimodularity forces its exponent
to be one:

```
g_u(v,w)-gamma=v^e H(v,w),           H irreducible.  (12)
```

At level `gamma`, the reduced special set `Y_gamma` is the union of the
shared line `L=V(v)` and the curve `C=V(H)`.  Formula (2) gives

```
chi(C)=chi(C intersect L)
      = number of distinct roots of H(0,w).           (13)
```

The last polynomial is nonzero (otherwise `H` would be associated to
`v`).  Since every irreducible affine curve has Euler characteristic at
most one, (13) leaves precisely two numerical possibilities:

```
H(0,w) has one distinct root and chi(C)=1,
```

or

```
H(0,w) is a nonzero constant and chi(C)=0.            (14)
```

Equations (10)--(14) are an unconditional reduction of the constant-node
case.  The remaining plane-pencil classification is supplied by Suzuki's
classification of `G_m`-polynomials on `A2`: if a polynomial has general
fiber `G_m`, then, up to a plane automorphism and a nonzero scalar, it is

```
s^i (s^l t-Q(s))^j,   gcd(i,j)=1, l>=0, deg Q<l.     (15)
```

(One convenient precise reference is Proposition 3.9 of M. Leuenberger,
*Complete algebraic vector fields on Danielewski surfaces*, Ann. Inst.
Fourier 66 (2016), where the result is attributed to Suzuki.)

Although the cited statement is written over `C`, it applies over every
algebraically closed field of characteristic zero by the usual Lefschetz
principle: spread the finitely many coefficients to a finitely generated
subfield, embed it in `C`, and express the resulting finite-degree
automorphism, its inverse, and the normal-form identity by polynomial
equations in their coefficients.  A solution over `C` gives one over the
algebraic closure inside `k` by the Nullstellensatz.

Apply this to `g_u-gamma=v^eH`.  The two components and their
multiplicities are `e` and `1`, so (after choosing the order of the two
normal-form components) `(i,j)=(e,1)`.  Moreover the component `v=0` is
the affine-line component.  The classifying automorphism may therefore be
oriented so that `s` generates the ideal `(v)`, hence `s=lambda v`.  Pulling
the second coordinate back gives a coordinate `W` with

```
H(v,w)=mu (v^l W-Q(v)).                              (16)
```

Thus the potentially singular or exotic alternatives left by Euler
characteristic alone are excluded by the `G_m`-pencil classification.

### Two rectifiable terminal forms

The reduction does immediately close the standard embeddings occurring in
both alternatives.  Equations (11)--(12), and absorption of a multiple of
`uv` into `x`, put the ambient polynomial (after scaling and subtracting
`gamma`) in the form

```
f = u(1+vX)+v^e H(v,w).                              (17)
```

If a change of the `w` coordinate fixing `v` writes

```
H(v,w)=P(v)+v^k W,   k>=0,                           (18)
```

then

```
f = v^e P(v) + (1+vX)u + v^(e+k) W.                 (19)
```

The row

```
(1+vX, v^(e+k)) in k[v,X]^2
```

is unimodular.  Explicitly, for `N=e+k`,

```
(1-vX+...+(-vX)^(N-1))(1+vX)
  + (-1)^N X^N v^N = 1.
```

Completing this row to an `SL_2(k[v,X])` matrix gives a linear
`k[v,X]`-automorphism in `(u,W)` whose first component is (17), up to the
harmless translation by `v^eP(v)`.  Hence `f` is a coordinate.

This argument includes:

* the first case of (14) whenever `C=V(H)` is actually a smooth embedded
  `A1`: then `H` is a plane coordinate, and the compatibility lemma with
  its degree-one restriction at `v=0` gives (18) with `k=0`;
* the hyperbolic case forced by Suzuki's normal form, including `H=1+vw`
  from the displayed example.

Consequently the constant-node case with the **squarefree coefficient**
`a=uv` is completely rectified as well.  Together with the main theorem,
this proves without any condition on `G(0,0,w)`:

**Corollary.** If

```
f=uvx+G(u,v,w),   R=B[f],
```

then `f` is a coordinate and `B=k^[3]`.

For `a=u^m v^n` with `m+n>2`, the nonconstant-node theorem still applies,
but at a constant node the remainder known only to be divisible by `uv`
cannot in general be absorbed into the term `u^m v^n x`.  The higher
infinitesimal jets along the nonreduced coefficient divisor are therefore
a separate remaining obstruction.

Even in those cases the generic divisor lemma, the coupled boundary
valuation matrices at exceptional node levels, and the all-level Euler
identity remain unconditional necessary conditions.  A counterexample of
this affine-modification form would have to satisfy these three compatible
systems, including the higher infinitesimal jets not seen by the reduced
boundary curves.  No such cancellation example is constructed here.

## 7. Adversarial audit of the direct constant-node proof

The direct proof in `counterexample_round2.md`, Section 5, avoids invoking
the full Suzuki normal form.  Its three delicate steps are valid, for the
following reasons.

### 7.1 The localization lattice really is an isomorphism

At the special level put `A=R/(f-gamma)` and `S={(uv)^N}`.  The
localization sequence for a normal noetherian domain is

```
A^* -> A_S^* -> direct_sum_(P subset V(uv), ht P=1) Z[P]
    -> Cl(A) -> Cl(A_S) -> 0.
```

Here

```
A^*=k^*,                    Cl(A)=0,
A_S=k[u^(+-1),v^(+-1),w],  Cl(A_S)=0,
A_S^*/A^*=<u,v> ~= Z^2.
```

Therefore the divisor map from the lattice generated by `u,v` onto the
free lattice of boundary primes is not merely surjective: it is an
isomorphism.  In particular there are exactly two boundary primes and the
valuation matrix lies in `GL_2(Z)`.  Once the `A1` branch is
`g_v-gamma=lambda u`, the matrix is

```
[[e,1],
 [d,0]],
```

so `d=1`.  There is no hidden class-group or unit assumption in this
calculation.

### 7.2 Smoothness of the threefold forces smooth axial curves

Let `F=uvx+G-c`, and consider a purported singular point `(v_0,w_0)` of
`g_u-c=0` with `v_0!=0`.  On `u=0`,

```
F_v=(g_u)_v=0,   F_w=(g_u)_w=0,   F_x=0,
F_u=v_0 x+G_u(0,v_0,w_0).
```

Choosing

```
x=-G_u(0,v_0,w_0)/v_0
```

makes the whole gradient vanish, contradicting smoothness of `R/(f-c)`.
Thus every nonspecial axial curve in
`Gm_v x A1_w` is smooth.  Its Euler characteristic zero and irreducibility
therefore identify it with `Gm`.

### 7.3 The etale and Laurent-derivative steps

On such a curve `C=Gm_t`, the restriction of `v` is a unit, hence

```
v|_C=lambda t^N.
```

It is nonconstant: otherwise the irreducible fiber would be a vertical
`A1`, not `Gm`.  Since `N!=0` and the characteristic is zero, this map
`C->Gm_v` is etale.  For the smooth plane curve `g=c`, ramification of
the projection to `v` occurs exactly where `partial_w g=0`.  As every
level `c!=gamma` is unramified,

```
V(partial_w g) intersect (Gm x A1)
  subset V(g-gamma) intersect (Gm x A1).
```

In `L=k[v^(+-1),w]`, `g-gamma` is a unit times one irreducible `p`.
Every nonunit irreducible factor of `partial_w g` would consequently be
associated to `p`, impossible by strict `w`-degree drop.  The derivative
is not zero (otherwise the generic fiber is a union of vertical affine
lines), so

```
partial_w g=rho v^r.
```

Since `g` is polynomial and `g(0,w)` is constant, `r>=1`, and integration
gives

```
g=rho v^r w+beta(v).
```

Thus the direct proof of the squarefree crossing theorem passes this
audit independently of the Suzuki classification.

## 8. What changes for `u^m v^n`: the higher-jet frontier

The same reduced-divisor analysis gives, after interchanging the axes if
necessary and normalizing constants,

```
f=u^m v^n x + lambda u + rho v^r w + beta(v)
  + uv H(u,v,w),                                    (20)
```

with `lambda rho!=0` and `r>=1`.  The class-group, smoothness, etale, and
Laurent arguments above are unchanged: none of them sees the nilpotent
thickness of `V(u^m v^n)`.  The obstruction is exactly the last summand.

For `m=n=1`, it is absorbed by `x->x+H`.  In general only the portion

```
H in u^(m-1)v^(n-1) k[u,v,w]
```

can be absorbed this way.  Equivalently, after this elementary move the
unresolved data are the finite transverse orders in the two strips

```
ord_u(H)<m-1   or   ord_v(H)<n-1.                    (21)
```

This is not a cosmetic gap.  For example

```
F=u^2 v x+u+v^2 w+uv w^2                            (22)
```

has exactly the shape (20).  After the renaming

```
(u,v,w,x)=(y,x,z,U),
```

it becomes

```
y+x(xz+y(yU+z^2)),
```

the first Vénéreau polynomial.  Thus a general elimination of (21) would
already contain the nontrivial Vénéreau/residual-coordinate mechanism;
reduced divisor theory alone cannot provide it.

More precisely, the literature proves that this polynomial is a
hyperplane and a one-stable coordinate, while its coordinateness in the
four-variable ring is the exceptional first Vénéreau case not covered by
the standard `n>=2` rectifications (see Lewis, arXiv:1007.2230, and
Blanc--Poloni, arXiv:2004.10739).  This does **not** make (22) a
counterexample to the present cancellation hypothesis: being a hyperplane
only identifies `R/(F)` abstractly with `k^[3]`, whereas `R=B[F]` requires
an embedded polynomial complement.  It does show rigorously that the
normal form (20), without using the extra splitting/slice datum, is too
broad to admit an elementary universal coordinate argument presently.

There are still elementary terminal subfamilies.  If `m=1` and, after
absorbing the divisible part, `H` belongs to `k[v,x]` (so it is independent
of `u,w`), then

```
f-beta(v)
 = (lambda+vH+v^n x)u + rho v^r w.
```

The coefficient row over `k[v,x]` is unimodular because its first entry is
`lambda mod v`; completing it to `SL_2(k[v,x])` makes `f` a coordinate.
The symmetric statement holds when the multiplicity-one axis is the other
one.  Beyond such affine-row cases, (20)--(21) is the exact audited
frontier; no argument here claims that the higher jets are removable.

## 9. Closure of the higher jets by a two-stage fibration

The preceding frontier is superseded once one uses the quotient algebra,
rather than trying to absorb the jets by an ambient elementary
automorphism.

**Theorem (all crossing multiplicities).** Suppose

```
f=u^m v^n x+G(u,v,w),   m,n>=1,   R=B[f].
```

Then `B=k^[3]` and `f` is a coordinate.

The nonconstant-node case was proved in Section 4.  In the constant-node
case, Sections 6--8 (or the direct proof audited in Section 7) give, after
interchanging the axes and making plane coordinate changes, the normal
form

```
f=u^m v^n x+lambda u+rho v^r w+beta(v)+uvH(u,v,w),  (23)
```

where `lambda rho!=0` and `r>=1`.  Crucially, `H` has no `x` dependence,
because the original remainder `G` did not.

Replace `f` by `f-beta(0)`.  This does not change the hypothesis
`R=B[f]`, and the quotient by the new polynomial is again abstractly `B`
(it is evaluation of the polynomial variable at `beta(0)`).  Thus assume

```
beta(0)=0,
A=R/(f) ~= B.
```

### 9.1 Every `v`-fiber is an affine plane

At `v=0`, equation (23) reduces to `lambda u=0`, hence

```
A/(v)=k[x,w]=k^[2].                                  (24)
```

Fix `c in k^*`.  The fiber is the affine surface

```
S_c=Spec k[x,u,w]/(
 c^n u^m x+lambda u+rho c^r w+beta(c)
 +uc H(u,c,w)).                                      (25)
```

Project it to `A1_u`.  If `u!=0`, the coefficient `c^n u^m` eliminates
`x`, leaving the free coordinate `w`.  At `u=0`, the equation is

```
rho c^r w+beta(c)=0,
```

which eliminates `w` and leaves the free coordinate `x`.  Thus every
geometric fiber over `u` is `A1`.

There are no concealed flatness or smoothness assumptions here.  The
polynomial in (25), regarded as a degree-one polynomial in `x` over the
UFD `k[u,w]`, is primitive: its coefficient is `c^n u^m`, while its
constant term is not divisible by `u` because its reduction modulo `u` is
the nonzero linear polynomial `rho c^r w+beta(c)`.  Hence `S_c` is a
domain, so its coordinate ring is torsion-free, and therefore flat, over
the PID `k[u]`.  Relative smoothness is also visible directly:

* for `u!=0`, the relative derivative with respect to `x` is nonzero;
* for `u=0`, the relative derivative with respect to `w` is `rho c^r!=0`.

Thus `S_c->A1_u` is a smooth affine-line fibration.  The
Kambayashi--Miyanishi--Wright theorem makes it an affine-line bundle; on
`A1`, `Pic=0` and `H^1(O)=0`, so it is trivial.  Consequently

```
S_c ~= A2                                             (26)
```

for every `c!=0`.  The argument is algebraic and remains valid after any
residue-field extension.

The generic `v`-fiber must also be checked.  Over `K=k(v)`, the same
projection to `A1_(K,u)` has affine-line fibers: `v` and `rho v^r` are
units, so the identical elimination applies.  The characteristic-zero
affine-line fibration theorem over `K[u]` gives

```
A tensor_(k[v]) K ~= K^[2].                           (27)
```

### 9.2 The affine-plane fibration over `A1_v` is trivial

The map `k[v]->A` is injective.  Indeed a nonzero polynomial in `v`
cannot lie in `(f)`, by comparison of degrees in `x`.  Since `A` is a
domain, it is torsion-free, hence flat, over the PID `k[v]`.  Equations
(24), (26), and (27) say that every scheme-theoretic geometric fiber is an
affine plane.  Thus `A` is an `A2`-fibration over `k[v]`.

For completeness, the standard triviality route used here is local and
has exactly the required hypotheses.  Localize at any maximal ideal
`(v-c)` of `k[v]`.  The base is a characteristic-zero DVR, the algebra is
finitely presented and flat, and both its generic and special fibers are
polynomial rings in two variables.  Sathaye's DVR theorem (*Polynomial
ring in two variables over a DVR: a criterion*, Invent. Math. 74 (1983),
Theorem 1) therefore gives

```
A_(v-c) ~= k[v]_(v-c)^[2].
```

Hence `A` is a locally polynomial `k[v]`-algebra.  The
Bass--Connell--Wright theorem for finitely presented locally polynomial
algebras identifies it with `Sym_(k[v])(P)` for a rank-two projective
`k[v]`-module `P`.  The PID property makes `P` free.
Therefore

```
A=k[v]^[2]=k^[3].                                    (28)
```

Since `A~=B` and `R=B[f]`, a polynomial basis of `B` together with `f`
is a polynomial basis of `R`.  Thus `f` is an ambient coordinate.

### 9.3 Audit verdict

The higher term `uvH` causes no problem: it vanishes precisely on the
`u=0` chart where `w` is eliminated, and away from that chart the term
`u^m v^n x` eliminates `x`.  No divisibility of `H` by
`u^(m-1)v^(n-1)`, no control of its degree, and no ambient rectification of
Vénéreau-type jets is needed.  The proof uses the splitting assumption
exactly at the end, through `A~=B` and `R=B[f]`.
