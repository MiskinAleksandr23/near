# Crossing-coefficient candidates: a complete no-go theorem

Let `k` be algebraically closed of characteristic zero and

```text
R=k[x,u,v,w].
```

This note tests the first coefficient which genuinely depends on two base
variables.  It gives a complete no-go result for a reduced transverse
crossing, including the initially exceptional constant-intersection branch.

## Theorem (the reduced crossing is impossible)

Suppose

```text
f=uvx+G(u,v,w),       R=B[f].                         (1)
```

Then `f` is a coordinate of `R` and `B=k^[3]`.

The proof uses all parallel fibers `f=c`, not merely the zero fiber.

## 1. Stable properties of every parallel fiber

For every `c in k`, translation in the polynomial variable of `B[f]`
gives

```text
B_c:=R/(f-c) ~= B.
```

Thus `B_c` is a smooth factorial domain, `B_c^*=k^*`, and its compactly
supported Euler characteristic is one.  The last assertion follows from

```text
Spec(B_c) x A1 ~= A4.
```

Put

```text
g_u(v,w)=G(0,v,w),
g_v(u,w)=G(u,0,w),
h(w)=G(0,0,w).
```

## 2. Factoriality forces all axial fibers to be integral and reduced

**Lemma 1.** If `h-c` is not the zero polynomial, then both `g_u-c` and
`g_v-c` are nonconstant, irreducible, and squarefree.

**Proof.** It suffices to treat `g_u-c`.  It cannot vanish identically,
because then `f-c` is divisible by `u`, contradicting that `B_c` is a
domain.  It cannot be a nonzero constant either: then `B_c/(u)=0`, so
`u` is a unit in `B_c`, contrary to `B_c^*=k^*`.  (The image of `u` is
not constant, for comparison of degrees in `x` shows that
`k[u,v,w] -> B_c` is injective.)

Factor

```text
g_u-c=lambda product_j p_j^(e_j)
```

in `k[v,w]`, with the `p_j` distinct irreducibles.  In `B_c` the ideals

```text
P_j=(u,p_j)
```

are height-one primes, since

```text
B_c/P_j ~= k[x,v,w]/(p_j).
```

Regularity makes `(B_c)_(P_j)` a DVR, and reducing the defining equation
modulo `u` gives

```text
ord_(P_j)(u)=e_j.                                     (2)
```

Because `h-c` is nonzero, no `p_j` is associated to `v`; hence `v` is a
unit at every `P_j`.  As `B_c` is factorial, write `P_j=(q_j)` for a
prime element.  After
inverting `uv`, equation (1) eliminates `x` and gives

```text
(B_c)_(uv)=k[u^(+-1),v^(+-1),w].
```

Hence `q_j` becomes a unit and, in the common fraction field,

```text
q_j=lambda_j u^a v^b,       a,b in Z.                 (3)
```

Taking valuations of (3) at every prime `P_l` above `u=0`, using that
`v` is a unit there, and using (2)
yields

```text
delta_(jl)=a e_l.
```

There can therefore be only one factor, and its exponent is one.  The
argument for `g_v-c` is symmetric.  QED.

## 3. Euler characteristic at the crossing

Let

```text
C_(u,c)=V(g_u-c) subset A2_(v,w),
C_(v,c)=V(g_v-c) subset A2_(u,w),
N_c=V(h-c) subset A1_w.
```

On the open set `uv!=0` of `Spec(B_c)`, eliminate `x`.  This open set is

```text
Gm^2 x A1
```

and has Euler characteristic zero.  Its closed complement is

```text
A1_x x Z_c,
Z_c=V(uv,G-c)=C_(u,c) union C_(v,c).
```

The intersection of the two curves is `N_c`.  Additivity therefore gives

```text
1=chi(B_c)=chi(C_(u,c))+chi(C_(v,c))-chi(N_c).          (4)
```

Suppose first that `h` has degree `d>=1`.  Choose `c` in a common dense open set
such that both axial curves are smooth and `h-c` has `d` distinct roots.
Lemma 1 makes both curves irreducible.  If a smooth irreducible affine
curve has completion of genus `q` with `s>=1` points at infinity, its
Euler characteristic is

```text
2-2q-s <= 1.
```

Equation (4) now says

```text
chi(C_(u,c))+chi(C_(v,c))=d+1.
```

The left side is at most two.  Consequently `d=1`, equality holds for
both curves, and both are isomorphic to `A1`.  By
Abhyankar--Moh--Suzuki, `g_u-c` and `g_v-c` are plane coordinates.
Therefore `g_u` and `g_v` are coordinates as well, and `h` is linear.

## 4. Simultaneous rectification along the two axes

We use the following elementary consequence of plane rectifiability.

**Lemma 2.** If `p(s,t)` is a coordinate of `k[s,t]` and `p(0,t)` has
degree one, then

```text
k[s,t]=k[s,p].                                         (5)
```

**Proof.** Choose a mate `q` with `k[s,t]=k[p,q]`.  In the `(p,q)`-plane,
the image of the line `s=0` is parametrized by `t`.  Since its first
coordinate `p(0,t)` is affine linear, the image is a graph
`q=Q(p)`.  The irreducible polynomial `s`, expressed in `k[p,q]`, thus
has the same reduced zero set as `q-Q(p)`; hence it is a nonzero scalar
multiple of `q-Q(p)`.  This proves (5).  QED.

Apply Lemma 2 to `g_v(u,w)` and to `g_u(v,w)`.  An automorphism of the
one-variable polynomial algebra `k[u][w]` over `k[u]` is affine in `w`,
and likewise over `k[v]`.  Since their common restriction is the same
linear polynomial `h(w)=lambda w+mu`, we obtain

```text
G(u,0,w)=lambda w+p(u),
G(0,v,w)=lambda w+q(v),
p(0)=q(0)=mu,       lambda!=0.                         (6)
```

The difference between `G` and the inclusion-exclusion expression of its
two axial restrictions is divisible by `uv`.  Thus for some
`H in k[u,v,w]`,

```text
G=lambda w+p(u)+q(v)-mu+uvH.
```

Replacing `x` by `x+H` in (1) gives

```text
f=uv(x+H)+lambda w+p(u)+q(v)-mu.
```

It is triangular in `w`, with nonzero constant coefficient `lambda`.
Therefore `f` is an ambient coordinate in the nonconstant-intersection
case.

## 5. The constant-intersection branch

The omitted case is not a technical oversight in Lemma 1.  If
`h(w)=gamma` is constant, the common prime `(u,v)` sees both `u` and `v`,
so the two valuation columns can cancel each other.  Nevertheless the
same argument gives a rather tight normal form.

Choose generic `c!=gamma`.  Lemma 1 applies, and (4), now with `N_c`
empty, gives

```text
chi(C_(u,c))+chi(C_(v,c))=1.                           (7)
```

Both terms are at most one.  For a generic smooth irreducible affine
curve, Euler characteristic one means `A1`, zero means `Gm`, and a
negative value cannot be paired in (7) with a term at most one.  Thus,
after interchanging `u,v`, the general fibers of `g_v(u,w)` are `A1`
and those of `g_u(v,w)` are `Gm`.

Abhyankar--Moh--Suzuki makes `g_v` a plane coordinate.  Since
`g_v(0,w)=gamma`, its fiber at `gamma` contains the whole line `u=0`;
a coordinate fiber is irreducible and reduced, hence

```text
g_v(u,w)=gamma+lambda u,       lambda in k*.           (8)
```

Subtracting the two axial restrictions and absorbing a multiple of `uv`
into `x` reduces (1) to

```text
f=uvx+lambda u+g(v,w),
g(0,w)=gamma,       general fiber of g is Gm.           (9)
```

There is a further exact UFD restriction.  Factor

```text
g-gamma=v^e product_(j=1)^s p_j^(d_j),
```

where no `p_j` is associated to `v`.  The height-one primes of `B_gamma`
over `uv` are the common prime `P_0=(u,v)` and
`P_j=(u,p_j)`.  The standard localization exact sequence for divisor
class groups says that the divisor vectors of the two units `u,v` in
`(B_gamma)_(uv)` must generate freely the group on all these primes,
because `B_gamma` is a UFD and its only original units are constants.
There are only two unit generators, so `s<=1`.  The case `s=0` is
incompatible with a general `Gm` fiber (`v^e-c` either splits for `e>1`
or is an affine line for `e=1`).  Hence `s=1`.  Locally at `P_0`, `v` is
a uniformizer and `ord_(P_0)(u)=e`; locally at `P_1`,
`ord_(P_1)(u)=d_1`.  Thus the divisor matrix of `(u,v)` in the ordered
basis `(P_0,P_1)` is

```text
[[e,1],
 [d_1,0]].
```

Surjectivity over `Z` forces its determinant to be a unit, so `d_1=1`.
Consequently the only residual shape is

```text
f=uvx+lambda u+gamma+v^e p(v,w),                       (10)
```

where `p` is irreducible, not divisible by `v`, and the general fiber of
`v^e p` is `Gm`.  Formula (10) looks at first like a residual frontier,
but the geometry of the nonspecial fibers closes it too.

In fact (7) and the absence of critical points of `f` show, for every
`c!=gamma`, that

```text
V(g-c) subset Gm_v x A1_w
```

is a smooth irreducible curve of Euler characteristic zero, hence is
`Gm`.  On this curve the restriction of `v` is a nonconstant unit.  Under
an isomorphism with `Gm_t`, it has the form

```text
v=lambda_c t^n,       n!=0,
```

and is therefore etale over `Gm_v`.  The projection to `v` can ramify on
`V(g-c)` only where `partial_w g=0`.  Consequently

```text
V(partial_w g) intersect (Gm x A1)
    subset V(g-gamma) intersect (Gm x A1).             (11)
```

In the Laurent UFD `k[v^(+-1),w]`, formula (10) says that `g-gamma` is a
unit times the irreducible `p`.  If `partial_w g` had a nonunit
irreducible factor, (11) would force that factor to be associated to `p`.
But

```text
deg_w(partial_w g) < deg_w(p)=deg_w(g-gamma),
```

which is impossible.  (The derivative cannot vanish identically, since
then a generic curve would be a disjoint union of affine lines, not
`Gm`.)  Hence `partial_w g` is a unit of the Laurent ring, and

```text
g(v,w)=rho v^m w+beta(v),
rho in k*,       m>=1,       beta(0)=gamma.             (12)
```

Substitute (12) in (9).  Over `A=k[v,x]`, the polynomial `f-beta(v)` is
the linear form in `(u,w)` with coefficient row

```text
(lambda+vx, rho v^m).                                  (13)
```

This row is unimodular.  Explicitly, with `T=vx/lambda`,

```text
(1+T) sum_(j=0)^(m-1)(-T)^j + (-T)^m =1,
```

and the last term is a multiple of `rho v^m`.  More explicitly, set

```text
P=lambda^(-1) sum_(j=0)^(m-1)(-vx/lambda)^j,
Q=(-1)^m x^m/(rho lambda^m).
```

Then `P(lambda+vx)+Q rho v^m=1`, so

```text
[[lambda+vx, rho v^m],
 [-Q,          P     ]]
```

lies in `SL_2(A)`.  It gives an `A`-linear automorphism in `(u,w)` whose
first component is `f-beta(v)`.  Adding back `beta(v)` preserves
coordinateness.  Thus `f` is a coordinate also when `h` is constant,
completing the theorem.

For orientation, the most elementary member

```text
u+v+uvx+v^2w
```

is still a coordinate: with `Delta=ux+v w`, the Anick shear

```text
U=u+v Delta,       W=w-x Delta
```

fixes `v,x,Delta`, is invertible, and the displayed polynomial is
`U+v`.

## 6. Nonreduced crossings: complete theorem

There is a useful extension which avoids all transverse-jet bookkeeping.
Suppose

```text
f=u^m v^n x+G(u,v,w),       max(m,n)>1,
```

and still `R=B[f]`.  If `h(w)=G(0,0,w)` is nonconstant, the divisor and
Euler arguments above are unchanged by the multiplicities `m,n`: they
force `h` to be linear and the two reduced axial restrictions to have
the form (6).

Consider

```text
X=Spec(R/(f)) -> A2_(u,v).
```

Every geometric fiber is `A1`.  Off `uv=0`, eliminate `x`, leaving the
free coordinate `w`.  On either axis, formula (6) fixes `w` uniquely and
leaves `x` free; the same is true at their intersection.

The coordinate ring of `X` is regular (indeed it is `B`) and hence
Cohen--Macaulay.  All fibers over the regular base `A2` have the expected
dimension one, so miracle flatness makes the displayed morphism flat.
Since all its geometric fibers are smooth affine lines, it is a smooth
`A1`-fibration.  The Kambayashi--Miyanishi--Wright local-triviality
theorem identifies such a fibration with an affine-line bundle.  Its
linear part lies in `Pic(A2)=0`, and its translation torsor lies in
`H^1(A2,O)=0`; it is therefore trivial.  Thus

```text
B=k[u,v]^[1]=k^[3],
```

and `R=B[f]` makes `f` a coordinate.

Hence arbitrary crossing multiplicities are excluded whenever the
intersection restriction is nonconstant.  It remains to consider

```text
max(m,n)>1,       G(0,0,w) constant.
```

Even here the reduced data admit the same classification as above.  The
generic Euler calculation gives one `A1` side and one `Gm` side.  After
interchanging the axes, Abhyankar--Moh--Suzuki gives

```text
G(u,0,w)=gamma+lambda u,       lambda!=0,
G(0,v,w)=g(v,w),
```

so inclusion--exclusion writes

```text
G=lambda u+g(v,w)+uvH(u,v,w).                         (15)
```

For clarity, the special-factor argument also survives the powers.
Factor `g-gamma=v^e product p_j^(d_j)`.  In `B_gamma`, the primes over
`uv` are `P_0=(u,v)` and `P_j=(u,p_j)`.  Localization at `uv` is still
the Laurent polynomial ring, whose units modulo constants have rank two;
the divisor-class localization sequence therefore gives at most two
such primes.  There must be a non-`v` factor: otherwise
`g-gamma` is a scalar times `v^e`, whose generic fiber is either reducible
(`e>1`) or `A1` (`e=1`), never the required `Gm`.  Thus there is exactly
one `p`.  At `P_0`, reduction modulo
`u` has multiplicity `e`, while reduction modulo `v` is the reduced
equation `lambda u=0`; hence `ord_(P_0)(u)=e` and
`ord_(P_0)(v)=1`.  At `P_1`, reduction modulo `u` has multiplicity
`d_1`, so the DVR length formula gives `ord_(P_1)(u)=d_1`, while `v` is
a unit.  The divisor matrix is again

```text
[[e,1],[d_1,0]],
```

and its surjectivity over `Z` forces `d_1=1`.

It remains to see that `g` is linear in `w`.  A generic curve `V(g-c)`
is the `Gm` side of the Euler dichotomy.  Its coordinate `v` is a
nonconstant unit, hence under `V(g-c)=Gm_t` it equals `a t^d` and defines
an etale map to `Gm_v`.  If an irreducible factor `q` of `partial_wg` in
`k[v^(+-1),w]` dominated the value line of `g`, it would meet a generic
fiber and give a ramification point, impossible.  Thus `g` is constant,
say `c_q`, on `V(q)`, and `q` divides `g-c_q`.  For `c_q!=gamma`, Lemma
1 makes this last polynomial irreducible; for `c_q=gamma`, its Laurent
part is the just-proved irreducible `p`.  In either case `q` would be
associated to a polynomial of `w`-degree `deg_wg`, contradicting
`deg_w(partial_wg)<deg_wg`.  Therefore `partial_wg` is a Laurent unit,

```text
partial_wg=rho v^r,       rho!=0, r>=1.
```

(Here `r>=1` follows from `g(0,w)=gamma`.)  Integrating gives the exact
form

```text
f=u^m v^n x+lambda u+rho v^r w+beta(v)+uvH(u,v,w),    (16)
lambda rho!=0,       r>=1,       beta(0)=gamma.
```

The apparent transverse-jet frontier (16) is also impossible.  Put
`C=R/(f)`, and consider the morphism

```text
Spec(C) -> A1_v.                                       (17)
```

The inclusion `k[v] -> C` is injective by comparison of `x`-degrees.
Since `C` is a domain, it is torsion-free and hence flat over the PID
`k[v]`.

Every geometric fiber of (17) is `A2`.  At `v=0`, equation (16) becomes

```text
lambda u+beta(0)=0,
```

which fixes `u` and leaves `(x,w)` free.  Fix now `v=c!=0`.  The fiber
surface is

```text
c^n u^m x+lambda u+rho c^r w+beta(c)
       +ucH(u,c,w)=0.                                 (18)
```

Project this surface to `A1_u`.  If `u!=0`, eliminate `x` and leave `w`
free.  If `u=0`, the nonzero coefficient `rho c^r` fixes `w` and leaves
`x` free.  Thus every geometric fiber over `u` is `A1`; the hypersurface
is Cohen--Macaulay and all fibers have pure dimension one, so miracle
flatness applies.  Kambayashi--Wright makes it an affine-line bundle over
`A1_u`, and `Pic(A1)=H^1(A1,O)=0` trivializes it.  Hence (18) is `A2`.

We have proved that `C` is an `A2`-fibration over the smooth curve
`A1_v`.  The characteristic-zero affine-plane-fibration theorem over a
smooth curve (Sathaye locally over every DVR, followed by
Bass--Connell--Wright) makes `C` a symmetric algebra of a rank-two
projective `k[v]`-module.  That module is free because `k[v]` is a PID.
Consequently

```text
C=k[v]^[2]=k^[3].
```

Finally the standing equality `R=B[f]` identifies `B` with `C`; hence
`B=k^[3]` and `f` is a coordinate.  Combining the two branches proves:

**Theorem 2.** For arbitrary `m,n>=1`, if

```text
f=u^m v^n x+G(u,v,w),       R=B[f],
```

then `f` is a coordinate and `B=k^[3]`.

### 6.1 An explicit jet-free quotient parametrization

There is no survivor in (16) if the transverse jet vanishes and the
one-variable tail is constant.  After scaling, it suffices to consider

```text
F=u+u^m v^n x+v^r w,       m,n,r>=1.                  (19)
```

We prove directly that `R/(F)=k^[3]`.  In the quotient put

```text
q_0=u^m x+v^(r-n)w
```

when `r>=n`; then `u=-v^nq_0` and

```text
q_0=(-1)^m v^(nm)q_0^m x+v^(r-n)w.                   (20)
```

If `r<n`, first absorb `v^r w` into the `u`-coordinate in the evident
triangular way after writing (19) as a unimodular two-term row; equivalently
one can interchange the first elementary step below.  Thus assume `r>=n`.

More generally, suppose at some stage an element `q_i` satisfies

```text
q_i=epsilon v^A q_i^m x+v^B w,       A>0, B>=0.       (21)
```

If `B=0`, then

```text
w=q_i-epsilon v^Aq_i^m x,
```

and the process is finished.  If `B>0`, set `s=min(A,B)` and define,
without any division in the quotient,

```text
q_(i+1)=epsilon v^(A-s)q_i^m x+v^(B-s)w.
```

Then `q_i=v^s q_(i+1)`, and substitution gives

```text
q_(i+1)=epsilon v^(A+(m-1)s)q_(i+1)^m x+v^(B-s)w.    (22)
```

The new first exponent remains positive, while the second exponent
strictly decreases.  Thus after finitely many steps (22) reaches `B=0`.
At that stage `w` is a polynomial in `(v,x,q_N)`; all preceding `q_i`
and then `u=-v^nq_0` are also polynomials in these three elements.
Consequently they generate `R/(F)`.  The resulting surjection

```text
k[v,x,q_N] -> R/(F)
```

is an isomorphism, since both sides are three-dimensional domains.

For `r<n`, a completely uniform initialization avoids the shorthand
above: write (19) as

```text
F=u+v^r(w+u^m v^(n-r)x)
```

and make the triangular change `w'=w+u^m v^(n-r)x`; then
`F=u+v^r w'` is a coordinate already.

Thus (19) cuts out `A3`.  Under the standing cylinder hypothesis
`R=B[F]`, this gives `B=k^[3]` and hence makes `F` an ambient coordinate.
This is an explicit special-case supplement to the general fibration
proof, not an additional hypothesis in Theorem 2.

### 6.2 Why the direct coordinate route still sees Vénéreau

The `uvH` term is not cosmetic for a proof that ignores the cylinder
hypothesis.  For every `N>=1`, specialize (16)
to

```text
V_N=u+u^2 v^N x+v^(N+1)w+u v^N w^2
   =u+v^N(vw+u(ux+w^2)).                               (23)
```

After renaming `(v,u,w,x)` as the customary `(x,y,z,u)`, this is exactly
the Vénéreau polynomial

```text
b_N=y+x^N(xz+y(yu+z^2)).
```

These polynomials are hyperplanes and strongly residual coordinates;
they are also one-stable coordinates.  The members `N>=2` are known to
be coordinates (the case `N=2` requires the nontrivial Lewis argument),
while `b_1` is the classical unresolved coordinate frontier in this
family.

This does **not** turn `b_1` into a cancellation counterexample.  A
hyperplane, or even a one-stable coordinate, does not provide a
decomposition `R=B[b_1]` in the original four-variable ring.  Such a
decomposition would itself make the whole family over the `b_1`-line
globally trivial and is strictly stronger than having individually
polynomial fibers.  Formula (23) explains why the direct ambient-
automorphism route meets a known hard embedding-coordinate problem,
whereas Theorem 2 succeeds by using the cylinder hypothesis to identify
the quotient through two successive affine-fibration arguments.

Primary references for this identification and status are
Kaliman--Zaidenberg, *Vénéreau polynomials and related fiber bundles*
(`arXiv:math/0308191`), and Lewis, *Vénéreau-type polynomials as potential
counterexamples* (`arXiv:1007.2230`) and *Strongly residual coordinates
over A[x]* (`arXiv:1304.1765`).

## 7. A reduced rectangular divisor

The nonconstant-node argument extends from one crossing to an arbitrary
reduced rectangular arrangement.  Let

```text
a(u)=product_(i=1)^r (u-alpha_i),
b(v)=product_(j=1)^s (v-beta_j)
```

up to nonzero scalar factors, with all roots distinct and `r,s>=1`, and
suppose

```text
f=a(u)b(v)x+G(u,v,w),       R=B[f].                    (14)
```

Set `h_ij(w)=G(alpha_i,beta_j,w)`.  If every `h_ij` is nonconstant, then
`f` is a coordinate.

Indeed, the valuation proof of Lemma 1 applies on every vertical and
horizontal component: no generic component factor can be supported at a
crossing because `h_ij-c` is a nonzero polynomial.  Hence for generic
`c`, all `r+s` component curves are smooth and irreducible, and each has
Euler characteristic at most one.

The open stratum `a(u)b(v)!=0` of `B_c` is

```text
(A1 minus r points) x (A1 minus s points) x A1
```

and has Euler characteristic `(1-r)(1-s)`.  The exceptional stratum is
`A1_x` times the union of the `r+s` component curves.  Their pairwise
intersections are the finite schemes `V(h_ij-c)`, and there are no triple
intersections.  For generic `c`, write `d_ij=deg h_ij`.  Inclusion--
exclusion gives

```text
1=(1-r)(1-s)+sum_i chi(C_i)+sum_j chi(D_j)-sum_ij d_ij,
```

or

```text
sum_i chi(C_i)+sum_j chi(D_j)
    =r+s-rs+sum_ij d_ij.                              (15)
```

The left side is at most `r+s`, while every `d_ij>=1`.  Thus both bounds
in (15) are equalities: every `d_ij=1` and every component curve is
`A1`.

Abhyankar--Moh--Suzuki and Lemma 2 show that on each vertical component

```text
G(alpha_i,v,w)=lambda_i w+p_i(v),
```

and on each horizontal component

```text
G(u,beta_j,w)=mu_j w+q_j(u).
```

Comparison at every grid point gives `lambda_i=mu_j`; connectedness of
the complete bipartite incidence graph makes all of them one scalar
`lambda in k*`.  Therefore `partial_wG-lambda` vanishes on every
component of `V(ab)`, so reducedness and coprimality give

```text
partial_wG-lambda in (ab).
```

Coefficientwise integration in `w` yields

```text
G=lambda w+K(u,v)+a(u)b(v)H(u,v,w).
```

Absorb `H` into `x`; the resulting expression is triangular in `w`.
This proves the claim.

## 8. Why the threefold truncation of the doubled KR candidate fails

A natural false-side attempt is to remove one center variable from the
doubled Koras--Russell fourfold.  For integers `m>=2`, `n>=1`, `d>=2`, put

```text
A_d=k[a,b,y,z]/(a^m b^n y+z^d+a).                    (24)
```

This is a smooth threefold: if `a=z=0`, the `a`-derivative is one (this is
where `m>=2` is used); if
`b=0` and `a!=0`, the equation cannot hold together with all remaining
partial derivatives.  It is also an affine modification with the same
crossing-coefficient flavor as the doubled KR candidate.  Nevertheless
its divisor class group gives an immediate stable obstruction.

After inverting `ab`, eliminate `y`:

```text
(A_d)_(ab)=k[a^(+-1),b^(+-1),z],
```

a UFD whose units modulo `k*` are freely generated by `a,b`.  The support
of the removed divisor has exactly two height-one primes,

```text
P=(a,z),
Q=(b,z^d+a).
```

At `P`, reduction modulo `a` is `z^d=0`, so the DVR length formula gives

```text
div(a)=dP.
```

At `Q`, reduction modulo `b` is the reduced irreducible equation
`z^d+a=0`, hence

```text
div(b)=Q.
```

The localization sequence

```text
(A_d)_(ab)^*/A_d^* -> ZP+ZQ -> Cl(A_d) -> 0
```

therefore has divisor matrix `diag(d,1)`.  (The same matrix also shows
that `A_d^*=k*`.)  Consequently

```text
Cl(A_d)=Z/dZ.                                         (25)
```

For a normal domain, adjoining a polynomial variable preserves the
class group, so

```text
Cl(A_d[T])=Z/dZ!=0.
```

Thus `A_d[T]` cannot be a polynomial ring.  This is a strict no-go, not
merely a failure to find a trivialization.  It also explains the extra
center variable in the factorial doubled KR fourfold: replacing `z^d`
on `a=0` by a reduced irreducible cusp such as `z^2+t^3` removes precisely
the multiplicity detected by (25), but necessarily raises the dimension.

The calculation is not special to a pure power.  If

```text
P(z)=product_(i=1)^s (z-alpha_i)^(e_i),
A_P=k[a,b,y,z]/(a^m b^n y+P(z)+a),       m>=2,
```

then the primes over `a=0` are `P_i=(a,z-alpha_i)`, with

```text
div(a)=sum_i e_i P_i,
```

and the single prime over `b=0` again occurs with multiplicity one.  The
same localization sequence gives

```text
Cl(A_P)=(Z^s / Z(e_1,...,e_s)).                        (26)
```

This is nonzero for every `deg P>=2`: it has free rank `s-1` when there
is more than one distinct root, and nonzero torsion when there is one
multiple root.  Thus in a threefold doubled-modification model with only
one residual center variable, factoriality itself forces `P` to be
linear.  A nonlinear reduced irreducible center is available only after
introducing at least a second residual variable, which again moves the
candidate to dimension four.

## 9. A three-component cycle leaves `2`-torsion

The first genuinely cyclic multi-node divisor also fails factoriality in
a very concrete way.  Let

```text
l_1=u,       l_2=v,       l_3=u+v-1,
P=u^2+v^2-u-v,
A_triangle=k[u,v,w,x]/(l_1 l_2 l_3 x+P).              (27)
```

The three lines form a triangle with vertices `(0,0),(0,1),(1,0)`.  On
each side, the restriction of `P` has exactly the two adjacent vertices
as simple zeros:

```text
P(0,v)=v(v-1),
P(u,0)=u(u-1),
P(u,1-u)=2u(u-1).
```

The hypersurface is a domain and is smooth.  Off the triangle this follows
from the nonzero `x`-derivative.  On it, points of the hypersurface are
exactly the three vertices, and the gradients of `P` there are respectively
`(-1,-1),(-1,1),(1,-1)`, all nonzero.  The variable `w` is passive.

After inverting `l_1l_2l_3`, eliminate `x`; the localization is the UFD

```text
k[u,v,(l_1l_2l_3)^(-1),w],
```

whose units modulo constants are generated by the three line equations.
The removed divisor has precisely the three height-one primes
`P_00,P_01,P_10` lying over the vertices.  In the ordered row basis
`(P_00,P_01,P_10)` and column basis `(l_1,l_2,l_3)`, their divisor matrix
is the unsigned incidence matrix

```text
M=[[1,1,0],
   [1,0,1],
   [0,1,1]].                                           (28)
```

Its determinant is `-2`.  The divisor-class localization sequence gives

```text
Cl(A_triangle)=coker(M)=Z/2Z.                          (29)
```

Therefore `A_triangle[T]` is never a polynomial ring.  The example is a
useful combinatorial warning for multi-component searches: an odd cycle
of reduced components with boundary primes at its nodes naturally
produces the unsigned incidence determinant `2` (an even cycle has
singular unsigned incidence matrix and leaves a free class instead).
Any factorial candidate
must break this cycle by adding further boundary primes/relations or by a
different center geometry; merely arranging smooth transverse nodes does
not suffice.

The same argument gives a small general lemma.  Suppose a connected
reduced SNC coefficient divisor has `r` components, every boundary prime
of the modification lies over a transverse pairwise node, and every such
prime occurs with multiplicity one in the two adjacent component
divisors.  If there are `N` nodes, the localization sequence is controlled
by the unsigned vertex--edge incidence map

```text
Z^r -> Z^N.
```

Having both only constant units and trivial class group would make this
map an isomorphism, so `N=r` and the incidence graph would be unicyclic.
Deleting attached tree vertices and edges reduces its determinant to that
of the unique cycle.  An even cycle has determinant zero; an odd cycle
has determinant of absolute value two.  It is never unimodular.

Hence no purely nodal reduced SNC modification of this kind can satisfy
simultaneously `A^*=k*` and `Cl(A)=0`.  A serious factorial candidate must
introduce at least one boundary prime supported in the interior of a
component, a prime incident to more than two components, or nonreduced
multiplicity data; a graph of smooth pairwise nodes alone is ruled out.
