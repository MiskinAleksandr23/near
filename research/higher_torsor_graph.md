# Higher-order coefficients for the basic torsor action

Let

```text
P=k[a,b,c,d],
q=b^2-2ac-1,
D(a)=0, D(b)=a, D(c)=b, D(d)=q,
r=ad-qb,
h=q^2c-qbd+ad^2/2,
C=ker D=k[a,q,r,h]/(2ah-r^2+q^2(q+1)).
```

For `w in P`, write `E_w=D+w partial_v` on `P[v]`.  This note gives
a graph criterion which applies to coefficients of arbitrary
`D`-order, and then a large exact no-go family whose invariant ring can
still be computed.

## 1. The orbit-integral criterion

Put

```text
Omega_w(x,t)=sum_{j>=0} t^(j+1) D^j(w)(x)/(j+1)!,
W_w(x,t)=Omega_w(x,t)/t.
```

Both sums are polynomials because `D` is locally nilpotent.  On the
action graph, with primes denoting the target endpoint,

```text
b'-b=ta,       d'-d=tq,       v'-v=t W_w.          (1)
```

Consequently, suppose there are polynomials `A(x,x'),B(x,x'),G(x,x')`
in the two endpoint coordinates such that, after pullback to the graph,

```text
1=Aa+Bq+G W_w                                  (2)
```

holds in `P[t]`.  Then the graph is a closed immersion: after replacing
`t a,t q,t W_w` by the three endpoint differences in (1), equation
(2) recovers `t` polynomially from the two endpoints.  (The endpoint
condition on the coefficients is essential; arbitrary coefficients in
`P[t]` would make this argument circular.)  The comorphism
of the graph therefore contains the source coordinates and `t`, hence
is surjective.  In particular the action is proper.

There is a useful genuinely higher-order application.  Let `lambda` be
`D`-invariant and suppose

```text
lambda in (a,q)P.                               (3)
```

For any `R in k[T]`, set

```text
w=1+lambda R(d).
```

If `d'=d+tq`, then

```text
W_w=1+lambda * (integral_0^1 R(d+s(d'-d)) ds).  (4)
```

The averaged polynomial, say `M_R(d,d')`, belongs to `k[d,d']`
(characteristic zero is used here).  Choose `A_0,B_0 in P` with
`lambda=aA_0+qB_0`.  Then the endpoint-polynomial identity

```text
1=W_w-a A_0 M_R(d,d')-q B_0 M_R(d,d')
```

has the required form (2).  We have proved:

> **Proposition.** Every action with coefficient
> `w=1+lambda R(d)`, where `lambda` is invariant and satisfies (3), is
> proper.  This includes `lambda=h psi(h)` and arbitrary nonlinear
> `R`; for `deg R>=2` one has `D^2(w) != 0` in general.

Adding a coboundary does not change this conclusion.  Indeed, for any
`u in P`, the triangular coordinate change

```text
v_0=v-u
```

conjugates `E_(w+D(u))` to `E_w`.  This observation is important: a
coefficient can have arbitrarily high `D`-order while defining exactly
the same torsor action as a low-order representative.

The proposition proves properness but, for nonlinear `R`, it does not
by itself decide whether the quotient is affine.  The next section is
an exact classification for a broad affine-linear subfamily, including
all of its arbitrary-order coboundary representatives.

## 2. Exact no-go family of arbitrary `D`-order

Fix

```text
psi in k[T]\{0},       alpha in k*,       beta in k,
lambda=h psi(h),
w_0=1+lambda(alpha d+beta),
w=w_0+D(u),             u in P arbitrary.                (5)
```

The polynomial `u` is unrestricted.  Hence `D^N(w)` may be nonzero for
any prescribed finite `N`, even though the coordinate shear above
reduces the action to `w_0`.

### Theorem

For every coefficient (5):

1. the `Ga`-action on `A5` is free and proper;
2. its invariant ring is the normal fourfold ring displayed below;
3. the canonical morphism from `A5` to the spectrum of that ring is
   not surjective;
4. the derivation has no slice, and its geometric quotient is not
   affine.

Thus arbitrary `D`-order obtained from a coboundary cannot repair the
nonaffine quotient in the `1+hd` construction.

### Properness

It is enough to use `v_0=v-u` and treat `w_0`.  Since

```text
h=a d^2/2+q(qc-bd),
```

we have `lambda in (a,q)P`.  The preceding proposition, with
`R(d)=alpha d+beta`, proves properness.  Freeness also follows from
the same Bezout identity: `(a,q,w_0)=P`, while `E(b)=a`, `E(d)=q`, and
`E(v_0)=w_0`.

### Explicit invariants

Define

```text
U=a v_0-b-lambda beta b-lambda alpha(bd-qc),
V=q v_0-d-lambda beta d-lambda alpha d^2/2.       (6)
```

Because `lambda` is invariant and

```text
D(bd-qc)=ad,       D(d^2/2)=qd,
```

both `U,V` are `E`-invariant.  A direct subtraction gives

```text
qU-aV=(1+beta lambda)r+alpha lambda h.             (7)
```

Let

```text
A_psi = k[a,q,r,h,U,V]/(
  2ah-r^2+q^2(q+1),
  qU-aV-(1+beta h psi(h))r-alpha h^2 psi(h)
).                                                   (8)
```

We next prove, rather than assume, that

```text
ker(E_w)=A_psi.                                      (9)
```

### Normality of the candidate ring

The two equations in (8) are a regular sequence.  After inverting
`q`, equation (7) eliminates `U`, leaving `C_q[V]`, a domain.  There is
no irreducible component contained in `q=0`: modulo `q`, the two
remaining equations

```text
2ah-r^2,
-aV-(1+beta h psi(h))r-alpha h^2 psi(h)
```

have no common factor in `k[a,r,h,U,V]`, so their common zero set has
dimension at most three, whereas every component of the complete
intersection (8) has dimension four.  Thus there is no minimal prime
containing `q`, and the domain `(A_psi)_q` shows that there is exactly
one minimal prime.  A complete intersection is Cohen--Macaulay and has
no embedded associated primes; hence `q` is a nonzerodivisor.  Any
nilpotent vanishes after inverting `q` and is therefore killed by a
power of `q`, so it is zero.  The unique minimal prime is consequently
zero, and `A_psi` is a domain.

The homomorphism from this abstract ring to `P[v_0]` defined by (6) is
injective.  It becomes the evident embedding `C_q[V] -> P_q[v_0]`
after inverting `q`; its kernel is therefore `q`-power torsion, while
`q` is a nonzerodivisor by the preceding paragraph.

For `R_1`, write the two equations as `F_1,F_2`.  The second gradient
has `U,V` entries `q,-a`.  If `(a,q)!=(0,0)` and the two gradients are
dependent, these entries force the proportionality factor to be zero.
Then `grad(F_1)=0`, which gives

```text
a=h=r=0,       q(3q+2)=0.
```

Neither possible nonzero value `q=-2/3` satisfies `F_1=0`, and `q=0`
contradicts `(a,q)!=(0,0)`.

If `a=q=0`, the first equation gives `r=0`, and the second gives

```text
alpha h^2 psi(h)=0.                                 (10)
```

At a nonzero root of `psi`, `grad(F_1)` has nonzero `a`-entry `2h`,
whereas the `r`-entry of `grad(F_2)` is `-1` (because `psi(h)=0`), so
the gradients are independent.  At `h=0`, `grad(F_1)=0`.  Therefore
the singular locus is exactly

```text
Pi=V(a,q,r,h) ~= A2_(U,V),
```

of codimension two.  The complete intersection is Cohen--Macaulay,
hence `S_2`, and the preceding calculation gives `R_1`; therefore
`A_psi` is normal.

### Exactness of the invariant ring

On `D(a)`, the element `s=b/a` is a slice.  Formula (6) changes
`(s,v_0)` triangularly to `(s,U/a)`, and hence

```text
(ker E)_a=C_a[U]=(A_psi)_a.                         (11)
```

On `D(q)`, the slice is `s=d/q`; formula (6) similarly gives

```text
(ker E)_q=C_q[V]=(A_psi)_q.                         (12)
```

By (10), the complement of `D(a) union D(q)` in `Spec(A_psi)` is a
finite union of two-dimensional planes (one for `h=0` and one for each
nonzero root of `psi`).  It has codimension two.  Normality and the
Krull/Hartogs intersection therefore imply

```text
A_psi=(A_psi)_a intersect (A_psi)_q
```

inside the common fraction field.  Every global invariant belongs to
both local kernels (11)--(12), proving (9).

### Missing boundary and absence of a slice

Let `y_0 in Spec(A_psi)` be the point

```text
a=q=r=h=U=V=0.
```

It has no preimage under the canonical invariant morphism.  Indeed,
`a=q=0` in `P` implies `b^2=1`; then `r=h=lambda=0`, and (6) gives

```text
U=-b in {1,-1},
```

never zero.  If `E_w` had a slice `S`, the slice theorem and (9) would
identify `P[v]=A_psi[S]`; the canonical morphism would be the
surjective projection of an affine line, contradicting the missing
point `y_0`.

In fact the whole affinization boundary is visible from the same
calculation.  Every point of `A5` with `a=q=0` has `r=h=0`, and its
image on `Pi` satisfies

```text
U=-b in {1,-1},       V=-d.
```

Thus the image meets the plane `Pi` only in the two lines `U=1` and
`U=-1`.  Moreover, every extra boundary plane in (10), corresponding
to a nonzero root of `psi`, is entirely missed because `a=q=0` in the
source always forces `h=0`.

Finally, properness gives a separated geometric quotient (as an
algebraic space).  If it were affine, the proper free action would be
a `Ga`-torsor over an affine base.  Its class would vanish in
`H^1(Y,O_Y)`, producing a global slice, which was just ruled out.
Thus the quotient is not affine.

## 3. What remains open in this branch

The graph calculation completely settles properness for the genuinely
nonlinear coefficients

```text
1+h psi(h) R(d),       deg R>=2,
```

and for all their coboundary translates.  The exact kernel computation
above uses the special primitives

```text
D(bd-qc)=ad,       D(d^2/2)=qd,
```

and therefore only covers affine-linear `R`.  For nonlinear `R`, the
`q`-chart still has an explicit invariant

```text
qv-d-h psi(h) integral R(d) dd,
```

but an analogous polynomial invariant on the `a`-chart need not
exist.  Deciding whether this changes the affinization boundary is the
remaining concrete question; properness alone does not decide it.

There is nevertheless a completely explicit first pair of invariants
for each monomial, which may be useful for that computation.  For

```text
w=1+lambda d^m,       lambda=h psi(h),       m>=2,
```

put

```text
U_m = a^(m+1)v-a^m b
      -lambda sum_(j=0)^m binom(m,j)
          r^(m-j) q^j b^(j+1)/(j+1),

V_m = qv-d-lambda d^(m+1)/(m+1).                  (13)
```

On `D(a)`, write `s=b/a`, so `d=r/a+qs`.  Formula (13) is just

```text
U_m=a^(m+1)(v-s-lambda integral (r/a+qs)^m ds),
```

and hence `E(U_m)=0`; directly `E(V_m)=0` as well.  Therefore

```text
qU_m-a^(m+1)V_m=a^m r+lambda J_m,                (14)
```

where the polynomial

```text
J_m = a^(m+1)d^(m+1)/(m+1)
      -q sum_(j=0)^m binom(m,j)
          r^(m-j) q^j b^(j+1)/(j+1)
```

is `D`-invariant and thus belongs to `C`.  This proves algebraically
that the two local quotient coordinates glue through an element of the
known invariant ring; no rational expression is hidden in (14).

However, the subring generated by `C,U_m,V_m` is not yet a plausible
full kernel: setting `a=q=0` in (14) leaves `h,U_m,V_m` free, a
codimension-one boundary.  In the affine-linear case the exceptional
identity `D(bd-qc)=ad` permits division by one power of `a` and changes
this boundary to codimension two.  For `m>=2` one must either find the
additional saturated generators or prove that this divisorial failure
is intrinsic.  This is the precise algebraic bottleneck left by the
nonlinear proper family.

One part of that bottleneck is intrinsic:

> **Primitive obstruction.** If `m>=2` and `psi!=0`, then
> `a h psi(h)d^m` does not belong to `D(P)`.

Indeed, after inverting `q` we have `P_q=C_q[d/q]`.  A primitive would
necessarily have the form

```text
T = a h psi(h)d^(m+1)/((m+1)q)+c,       c in C_q.
```

If `T` were in `P`, then

```text
c_0=qT-a h psi(h)d^(m+1)/(m+1)
```

would be both polynomial and `D`-invariant, hence would lie in `C`.
Reduction modulo `q` would say that the image of
`a h psi(h)d^(m+1)` belongs to the image of `C` in `P/(q)`.

That image is the monomial subring generated by

```text
a,       r=ad,       h=ad^2/2,
```

with the sole relation `r^2=2ah`.  Its monomial exponents `(A,B)` in
`a^A d^B` satisfy `B<=2A`.  If `c_l h^l` is a nonzero term of `psi`,
the corresponding term after reduction is a nonzero multiple of

```text
a^(l+2) d^(m+2l+3),
```

whose exponents satisfy `B-2A=m-1>0`.  Distinct `l` give distinct
monomials, so cancellation cannot help.  This contradiction proves the
obstruction.  In particular, unlike the linear case, there is no
invariant with leading `v`-coefficient `a` obtained by integrating the
nonlinear perturbation; the higher power `a^(m+1)` in (13) is forced.
