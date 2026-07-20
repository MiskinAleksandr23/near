# Classification of the invariant extensions of the basic free action

Let

```
P=k[a,b,c,d],
q=b^2-2ac-1,
D(a)=0, D(b)=a, D(c)=b, D(d)=q,
r=ad-qb,
h=q^2c-qbd+ad^2/2,
g=bd-2qc.
```

Then `D(q)=D(r)=D(h)=0`, `D(g)=r`, and

```
C=ker D=k[a,q,r,h]/(r^2-2ah-q^2(q+1)).
```

For completeness, the kernel equality follows from the two slice
presentations

```
P_a=C_a[b/a],             P_q=C_q[d/q].
```

The displayed hypersurface `C` is normal: its singular locus consists
only of the origin, of codimension three.  Moreover `V(a,q)` has
codimension two in `Spec C`.  Hence normality gives
`C=C_a intersect C_q` in its fraction field, and the two slice
presentations force every global `D`-invariant to lie in `C`.

Write `L=V(a,q,r) in Spec C`; then `L=Spec k[h]`.  For `w in C`, let
`phi(h)` be its image in `C/(a,q,r)=k[h]` and put

```
E_w=D+w partial_v
```

on `P[v]`.

## Theorem

1. If `phi(0)=0`, the action of `E_w` is not proper.
2. If `phi(0)!=0`, the action is proper and Zariski locally trivial.
3. Under (2), if `phi` is nonconstant, its geometric quotient is
   strictly quasi-affine and not affine.
4. Under (2), if `phi=c in k*`, then `E_w` has a global slice and its
   quotient is `A4`.

Thus no invariant coefficient `w` gives an affine non-polynomial
quotient.

## Proof of (1)

Use the DVR arcs

```
gamma_+(s)=(a,b,c,d,v)=(s,1,0,0,0).
```

On this arc `q=r=h=0` and `w=w(s,0,0,0)=O(s)`, since `phi(0)=0`.
For `s!=0`, apply the action with parameter `t=-2/s`.  The first four
coordinates become

```
(s,-1,0,0),
```

while the change in `v` is `tw`, which is integral and has a finite
limit.  At `s=0` the two limiting points cannot be in the same orbit:
`E_w(b)=a=0` there, so an orbit cannot change `b=1` into `b=-1`.
This violates the valuative criterion for properness.

## Proof of (2)

Since `C/(a,q,r)=k[h]`, there are `A,B,C_1 in C` such that

```
w=phi(h)+Aa+Bq+C_1r.                              (1)
```

As `phi(h)=phi(0)+h psi(h)`, while

```
r=ad-qb,   h=q(qc-bd)+ad^2/2,
```

formula (1) explicitly rewrites `w` as

```
phi(0) + a(A+C_1d+psi(h)d^2/2)
       + q(B-C_1b+psi(h)(qc-bd)).                 (2)
```

If `phi(0)!=0`, equation (2) gives, without Nullstellensatz,

```
(a,q,w)P=P.
```

The invariant principal opens `D(a),D(q),D(w)` have the local slices

```
b/a,   d/q,   v/w,
```

so the action is Zariski locally trivial.  It is also proper directly:
if `alpha a+beta q+gamma w=1`, then on the action graph

```
b'-b=t a,  d'-d=t q,  v'-v=t w,
```

and hence

```
t=alpha(b'-b)+beta(d'-d)+gamma(v'-v).
```

Here the Bezout coefficients are evaluated in the unprimed source
coordinates.  Thus the comorphism of the graph contains all source
coordinates and `t`, so it is surjective.  The graph morphism is a
closed immersion.

Let `K=ker E_w`.  On a principal open supplied with a slice, invariants
commute with localization.  Consequently the quotient is

```
D_Spec(K)(a) union D_Spec(K)(q) union D_Spec(K)(w),
```

an open subscheme of `Spec K`; in particular it is quasi-affine.

## Proof of (3)

Let `H!=0` be a root of the nonconstant polynomial `phi`.  Formula (1)
gives a stronger global simplification.  The triangular shear

```
v'=v-Ab-Bd-C_1g
```

makes `E_w(v')=phi(h)` everywhere, because
`a=D(b), q=D(d), r=D(g)`.  In particular `v'` is invariant on the
level `h=H`.

The quotient of `P/(h-H)` by `D` is `A2_(q,r)\{0}`.  Indeed

```
a=(r^2-q^2(q+1))/(2H),
```

and the two opens `D(a),D(q)` cover the punctured plane and have slices
`b/a,d/q`; their invariant rings are `k[q,r]_a,k[q,r]_q`.  Their
intersection gives the global invariant ring `k[q,r]`, but the origin
has no preimage because `a=q=r=0` would force `h=0` in `P`.

Consequently the closed level `h=H` of the geometric quotient is

```
(A2\{0}) x A1_(v'),
```

which is not affine: its global function ring is `k[q,r,v']`, whose
affine spectrum adds the missing line `q=r=0`.  A closed fiber of an
affine quotient would be affine, contradiction.  More explicitly, the
quotient map is a Zariski locally trivial `Ga`-torsor; after base change
by `h=H` it remains a torsor and its base is precisely the geometric
quotient just computed.  Thus no unjustified commutation of a general
categorical quotient with base change is being used.

## Proof of (4)

If `phi=c`, then `w-c` lies in the kernel of `C -> k[h]`, namely
`(a,q,r)`.  Write

```
w-c=Aa+Bq+Cr.
```

The element

```
s=(v-Ab-Bd-Cg)/c
```

satisfies `E_w(s)=1`.  The slice theorem gives
`P[v]=ker(E_w)[s]`; since `s` is an ambient coordinate after the same
triangular shear, `ker(E_w)=k^[4]`.
