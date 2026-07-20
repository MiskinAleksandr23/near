# Low-order non-invariant extensions of the basic Winkelmann action

Put

```text
P=k[a,b,c,d],  q=b^2-2ac-1,
D(a)=0, D(b)=a, D(c)=b, D(d)=q,
r=ad-qb, g=bd-2qc, D(g)=r.
```

For `w in P`, write `E=D+w partial_v` on `P[v]`.  Replacing `v` by
`v-u` replaces `w` by `w-D(u)`.

## The full switching boundary of the action graph

The one-parameter family used to detect nonproperness has more freedom
than the special arc `q=0`.  Fix `epsilon in {1,-1}` and arbitrary
`c0,c1,d0 in k`, and put

```text
a=s,
b=epsilon + beta*s,       beta=epsilon*(c0-c1)/2,
c=c0,
d=d0,
t=-2*epsilon/s.
```

Then, as `s -> 0`, the source and target of the action graph tend to

```text
x0=(0, epsilon,  c0, d0),
x1=(0,-epsilon,  c1, d0+2*epsilon*(c0+c1)).
```

Indeed

```text
t*a -> -2*epsilon,
t*b+t^2*a/2 -> c1-c0,
t*q -> 2*epsilon*(c0+c1).
```

The two limit points are never in one orbit of the special-fibre
action: at `a=0`, `D(b)=0`, whereas their `b`-coordinates are opposite.
Consequently, if the `v`-increment has a finite limit on one of these
arcs, `E` is not proper.

This corrects the insufficient test in which `q` was set identically
zero: the extra finite parameter `Q=lim(tq)=2 epsilon(c0+c1)` is
essential.

## Example: `w=1+bd` is not proper

Here `D^3(w)=0` and

```text
Delta(v)=t(1+bd)+t^2(ad+bq)/2+t^3*aq/3.
```

Take

```text
a=s, b=1, c=3/2, d=d0, t=-2/s.
```

Then `q=-3s`, so `ta=-2`, `tq=6`, and a direct substitution gives
`Delta(v)=0`.  The graph therefore has the two distinct limiting points

```text
(0, 1, 3/2, d0, v0),
(0,-1, 3/2, d0+6, v0),
```

which proves nonproperness.  Thus the apparently promising fact that
`w(0,1,c,d)+w(0,-1,c,d)=2` only checks the subfamily `Q=0` and is not a
properness criterion.

## A boundary criterion for all `D^2(w)=0`

Use the standard plinth ideal

```text
D(P) intersect ker(D)=(a,q,r) C,
C=ker(D).
```

If `D^2(w)=0`, then `D(w)` is invariant and hence

```text
w=F+A*b+B*d+C0*g,              (1)
```

for invariant coefficients `F,A,B,C0 in C`.  (Subtract the displayed
primitive of `D(w)=Aa+Bq+C0r`; the remainder is invariant.)

All invariants tend on a switching arc to the same point

```text
o=(a,q,r,h)=(0,0,0,0).
```

Because `D^2(w)=0`, the normalized increment is exactly the trapezoidal
average

```text
Delta(v)/t=(w(x0)+w(x1))/2.
```

Writing `X=c0+c1`, its boundary value, using (1), is

```text
K_boundary = F(o) + B(o)*d0 + (epsilon*B(o)-C0(o))*X.       (2)
```

Indeed the averages of `b,d,g` are respectively

```text
0,  d0+epsilon*X,  -X.
```

It follows immediately that a necessary condition for properness is

```text
F(o) != 0,   B(o)=0,   C0(o)=0.                            (3)
```

If any condition in (3) fails, choose `d0,X` so that (2) vanishes.  The
quantity `Delta(v)/t` is then a regular function of `s` with zero
constant term, hence is `O(s)`; since `t` has a simple pole,
`Delta(v)` is integral and has a finite limit.  The displayed graph arc
therefore proves nonproperness without any further recursive choice.
In particular, any coefficient of `d` or `g` which survives at the
exceptional invariant point forces nonproperness.

The coefficient of `b` does not appear in (2), consistently with
`b=D(c)`: it can be removed by the triangular shear `v -> v-Ac`.

## A rigorously proper genuinely non-invariant test: `w=1+h*d`

Let

```text
E=D+(1+hd) partial_v.
```

This action is proper.  Here is a direct valuative proof.  Suppose over
a DVR that both ends of an orbit segment are integral, while the group
parameter `t` has negative valuation.  The increments

```text
ta,  tq,  t*b+t^2*a/2
```

are integral.  Reduction modulo the maximal ideal forces

```text
a=q=r=h=0,  b^2=1;
```

otherwise either `tq` or `t(b+ta/2)` has a pole.  In particular `h`
has positive valuation, while `Q=tq` and both `d,d+Q` are integral.
But

```text
Delta(v)=t(1+hd)+t^2*hq/2
        =t*(1+h*(d+Q/2)).
```

The parenthesized factor is a DVR unit, so `Delta(v)` has a pole, a
contradiction.  Hence the action graph satisfies the valuative
criterion for properness.

There is also a shorter scheme-theoretic proof that the action graph is
a closed immersion.  Write primes for the target endpoint and put

```text
Delta(b)=b'-b=t*a,
Delta(d)=d'-d=t*q,
Delta(v)=v'-v=t*W,
W=1+h*(d+d')/2.
```

The invariant `h` lies in `(a,q)P`, explicitly

```text
h=a*d^2/2+q*(qc-bd).
```

Consequently there are polynomials `A,B` on the product of the two
copies of `A^5` such that

```text
1=W+A*a+B*q.
```

On the action graph this gives the polynomial recovery formula

```text
t=Delta(v)+A*Delta(b)+B*Delta(d).
```

The pullbacks of the first-endpoint coordinates together with this
polynomial generate the whole coordinate ring `k[a,b,c,d,v,t]` of
`Ga times A^5`.  Thus the ring map defined by the action graph is
surjective, so the graph morphism is a closed immersion and in
particular proper.  The same identity also shows freeness, since
`(E(b),E(d),E(v))=(a,q,1+hd)` is the unit ideal.

There are useful explicit local quotient coordinates.  Since

```text
a(1+hd)=D(b+h*(bd-qc)),
q(1+hd)=D(d+h*d^2/2),
```

the polynomials

```text
U=a*v-b-h*(bd-qc),
V=q*v-d-h*d^2/2
```

are `E`-invariant, and a direct calculation gives

```text
qU-aV=r+h^2.                                      (4)
```

On the closed invariant level `h=H!=0`, the quotient is the affine
torsor over `A^2_(q,r)\{0}` with Cech class

```text
(r+H^2)/(a*q),  a=(r^2-q^2(q+1))/(2H),
```

and affine equation (4).  Thus any failure of global affineness is
concentrated over `h=0`, exactly where the original nonseparated
switching occurs.

In fact the invariant ring and the obstruction over `h=0` can be
computed exactly.  Recall the standard presentation

```text
C=ker(D)=k[a,q,r,h]/(2ah-r^2+q^2(q+1)).
```

Set

```text
A_0=C[U,V]/(qU-aV-r-h^2).
```

Then

```text
ker(E)=A_0.                                             (5)
```

Here is a proof which also rules out hidden invariants supported over
`(a,q)`.  After inverting `a`, put `s=b/a`.  The old action has
`P_a=C_a[s]`, while `E(s)=1`; the formula for `U` recovers `v` from
`C_a[U,s]`.  Hence

```text
(ker E)_a=C_a[U]=(A_0)_a.
```

After inverting `q`, put `s=d/q`.  Similarly `P_q=C_q[s]`, `E(s)=1`,
and the formula for `V` recovers `v`, so

```text
(ker E)_q=C_q[V]=(A_0)_q.
```

The abstract ring `A_0` is a four-dimensional complete intersection:

```text
2ah-r^2+q^2(q+1)=0,
qU-aV-r-h^2=0.                                        (6)
```

Its Jacobian has rank less than two precisely on

```text
Pi=V(a,q,r,h) ~= A^2_(U,V).
```

Indeed the second gradient never vanishes because its `r`-entry is
`-1`.  If the two gradients are dependent and `(a,q)!=(0,0)`, their
`U,V` entries force the proportionality scalar to be zero.  The first
gradient would then give `a=h=r=0` and `q(3q+2)=0`; the only possible
nonzero value `q=-2/3` contradicts the first equation in (6).  On
`a=q=0`, equations (6) force `r=h=0`, and the rank is one.  Thus the
singular locus has codimension two.  The complete intersection is
`S_2` and is regular in codimension one, hence is normal.  (The dense
open set `q!=0`, equal to `Spec(C_q[V])`, is irreducible, while
`dim(A_0/(q))=3`; hence the equidimensional complete intersection has
no additional component supported on `q=0` and is a domain.)

The complement of `D(a) union D(q)` in `Spec(A_0)` has codimension two.
Normality therefore gives the Hartogs/Krull intersection

```text
A_0=(A_0)_a intersect (A_0)_q
```

inside the common fraction field.  Every global `E`-invariant belongs
to the two displayed local kernels, proving (5).

Now let `y_0` be the point of `Spec(A_0)` at which

```text
a=q=r=h=U=V=0.
```

It has no preimage in `A^5`.  Indeed `a=q=0` in `P` implies `b^2=1`,
and then the defining formula for `U` gives `U=-b`, hence `U=1` or
`U=-1`, never zero.  If `E` had a slice `S`, the slice theorem would
give `P[v]=(ker E)[S]`; the canonical morphism
`A^5 -> Spec(ker E)` would then be the surjective projection of an
affine line.  The missing point `y_0` is a contradiction.  Therefore

```text
E has no polynomial slice.                               (7)
```

More precisely, the image meets the boundary plane `Pi` only in the
two lines `U=1` and `U=-1` (with `V=-d` arbitrary).  The rest of `Pi`
is the affinization boundary created by the switching at `h=0`.

Since the action is free and proper, its geometric quotient exists as
a separated algebraic space.  It is not affine: if it were affine,
faithfully flat descent for the `Ga`-torsor would identify it with
`Spec(ker E)=Spec(A_0)`, forcing the quotient map to be surjective,
again contradicting the missing point `y_0`.

Thus the earlier bounded computation (no slice of total degree at most
12 over `F_1000003`) was detecting a genuine obstruction, not merely a
high-degree slice.  The formal `h`-adic slice starts

```text
v+h*(-vd+q*v^2/2)+...
```

and (7) proves that no choice of corrections can terminate.

## Logical restriction on the requested outcome

If a free `Ga`-action is Zariski locally trivial and its geometric
quotient `Y` is affine, then the torsor is automatically trivial:

```text
H^1_Zar(Y,O_Y)=0.
```

Hence there is necessarily a global slice.  So an "affine quotient but
no slice" cannot occur in this setup.  A cancellation counterexample
would instead be a proper action with affine quotient and a global
slice whose kernel is an exotic stably polynomial fourfold.

## The `w=c^2` test does not produce a counterexample

For `p=q+1=b^2-2ac` and `E(v)=c^2`, the polynomial

```text
S=-(p+1)d+b^3c-(7/2)abc^2+(15/2)a^2v
```

satisfies `E(S)=1`: the last three terms have derivative `p^2`, while
the first has derivative `1-p^2`.

Moreover `S` is an ambient coordinate.  It has the form

```text
S=(15/2)a^2 v+P(a,b,c,d),
```

and modulo `a`,

```text
P(0,b,c,d)=b^3c-(b^2+1)d.
```

The coefficients `b^3` and `b^2+1` are coprime, so the latter is a
coordinate of `k[b,c,d]` by an explicit unimodular `GL_2(k[b])`
change in `(c,d)`.  The standard one-variable Russell--Sathaye/Maubach
lifting criterion then makes `S` a coordinate of the full polynomial
ring.  The same reduction works for `w=c^m`: modulo `a`, the two
coefficients are `b^(2m-1)` and `sum_{i=0}^{m-1} b^(2i)`, which are
coprime.  Thus the entire pure-monomial family collapses to `A^4`.

## A larger genuinely `d`-dependent family also collapses

Let `lambda in C=ker(D)` be arbitrary and set

```text
E(v)=c+lambda*d.
```

The formula previously found for constant `lambda` in fact needs only
`D(lambda)=0`:

```text
S=bc-d-3av+3lambda*(bd-qc),
E(S)=1.                                                (8)
```

This slice is an ambient coordinate for every invariant `lambda`.
Indeed (5) has coefficient `-3a` in `v`, so it suffices by the
one-variable lifting criterion to check its reduction modulo `a`.
There put

```text
z=bc-d,  T=bd-qc.
```

Since `q=b^2-1` modulo `a`, one has `T=c-bz`; moreover all invariants
modulo `a` are functions of `b,T` (in particular
`h=q(qc-bd)=-qT`).  Hence

```text
S_bar=z+3*T*lambda_bar(b,T).
```

The changes `(c,z) -> (T,z)` and then
`(T,z) -> (T,S_bar)` are triangular automorphisms over `k[b]`.
Thus `S_bar` is a coordinate, and so is `S`.  This rules out, in one
stroke, arbitrary invariant `d`-perturbations of the first strong
properness term `c`.

In fact the same calculation gives the natural full low-order theorem.
Let `alpha in k*` and let `F,A,B,C0 in C`.  For

```text
w=alpha*c+F+A*b+B*d+C0*g                         (6)
```

first shear `v` to `v-Ac`, removing `A*b=D(Ac)`.  With

```text
z=bc-d,  T=bd-qc,  J=bg-rc
```

one has

```text
D(z)=1+3ac,  D(T)=ad,  D(J)=ag.
```

Therefore

```text
S=z-(3a/alpha)*(v-Ac)
    +(3/alpha)*(B*T+F*b+C0*J)
```

satisfies `E(S)=1`.  It is again a coordinate.  Modulo `a`, the above
coordinates give `T=c-bz` and `J=bT`, while the reductions of all
invariant coefficients are functions of `(b,T)`.  Thus

```text
S_bar=z + function(b,T),
```

a triangular coordinate; the lifting criterion applies as before.

Consequently every order-three extension whose genuinely divergent
`c`-coefficient is a nonzero constant and whose remainder has
`D^2=0` is rectifiable, even with arbitrary invariant `d` and `g`
coefficients.  A possible counterexample in `D^3(w)=0` must therefore
use a nonunit invariant coefficient of `c`; properness only sees that
coefficient at the exceptional point, while its zero levels are the
likely source of nonaffine quotient fibres.
