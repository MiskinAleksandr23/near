# Cancellation with a monomial crossing coefficient

Let `k` be algebraically closed of characteristic zero and

```text
R=k[x,u,v,w],
f=u^m v^n x+G(u,v,w),   m,n>=1,
R=B[f].
```

## Theorem

Then `B=k^[3]` and `f` is a coordinate of `R`.

The proof combines the all-parallel-level divisor/Euler argument with a
final `A2`-fibration that uses the splitting hypothesis essentially.

## 1. Parallel levels and the two axial pencils

For every `c in k`, `B_c=R/(f-c)` is isomorphic to `B`.  Thus it is a
smooth UFD with units `k*` and `chi_c(B_c)=1`.  Put

```text
g_u(v,w)=G(0,v,w),
g_v(u,w)=G(u,0,w),
h(w)=G(0,0,w).
```

If `h` is nonconstant, the generic-level valuation argument is clean:
no prime over one axis contains the other.  Hence both generic axial
curves are smooth irreducible.  Inclusion-exclusion gives

```text
1=chi(V(g_u-c))+chi(V(g_v-c))-deg(h).
```

Each curve has Euler characteristic at most one, so `deg(h)=1` and both
curves are `A1`.  AMS and compatibility with the common linear
restriction give

```text
g_u=lambda w+q(v),   g_v=lambda w+p(u),   lambda!=0.
```

For `X=Spec(B)->A2_(u,v)`, every geometric fiber is now `A1`: off the
axes eliminate `x`, and on the axes eliminate the linearly occurring
`w`.  Regularity plus equidimensionality gives flatness, so this is a
smooth `A1`-fibration.  It is a trivial affine-line bundle over `A2`
because `Pic(A2)=H^1(A2,O)=0`.  Thus `B=k^[3]`.

It remains to treat constant `h`.

## 2. The constant node has an exact normal form

Replace `f` by `f-h` and assume `h=0`.  At a generic nonzero level, the
two axial curves are disjoint and their Euler characteristics sum to one.
They are smooth irreducible curves of Euler characteristic at most one;
therefore their types are exactly `(A1,Gm)`.  Interchange `u,v` if
necessary.  The `A1` pencil is a plane coordinate, and its zero fiber
contains the whole axis, so

```text
g_v(u,w)=lambda u,   lambda in k*.                   (1)
```

Write `g=g_u`.  At the special level factor

```text
g(v,w)=v^e product_j p_j(v,w)^(d_j).
```

In the UFD `B_0`, the boundary primes over `uv` are the shared prime
`P_0=(u,v)` and the primes `P_j=(u,p_j)`.  Localizing at `uv` yields
`k[u^+-1,v^+-1,w]`; its unit lattice modulo `k*` has rank two, generated
by `u,v`.  The divisor localization sequence, with both class groups
zero, identifies this lattice with the free lattice on the boundary
primes.  Thus there is exactly one `p`, and the valuation matrix

```text
        P_0 P_1
div(u)  e   d
div(v)  1   0
```

is in `GL_2(Z)`.  Hence `d=1` and

```text
g=v^e p,   p irreducible.                            (2)
```

For a generic nonzero `c`, `V(g-c)` is `Gm`.  The unit `v` restricts to
`alpha t^N`, hence gives an etale map to `Gm`; consequently `g_w` has no
zero on a generic fiber.  Every irreducible component of `V(g_w)` in the
Laurent plane is therefore vertical for `g`.  If its value is `c!=0`,
the all-level UFD lemma makes `g-c` irreducible and reduced, so that
component would be associated to `g-c`, impossible from
`deg_w(g_w)<deg_w(g-c)`.  At value zero it would be associated to `p`,
with the same degree contradiction.  Therefore `g_w` is a Laurent unit:

```text
g=rho v^r w+beta(v),   rho!=0, r>=1, beta(0)=0.       (3)
```

Finally (1), (3), and inclusion-exclusion along the axes show that the
part of `G-lambda u-g` vanishes modulo both `u` and `v`, hence is `uvH`.
Every constant-node candidate has the exact form

```text
f=u^m v^n x+lambda u+rho v^r w+beta(v)+uvH(u,v,w).   (4)
```

## 3. The higher transverse jets disappear globally

This is the step missed by a purely ambient row calculation.  Identify

```text
B=R/(f)
```

and use the morphism `pi:Spec(B)->A1_v`.  The inclusion `k[v]->B` is
injective by comparison of `x`-degrees; since `B` is a domain, it is
torsion-free and hence flat over the PID `k[v]`.

Every geometric fiber of `pi` is `A2`.  At `v=0`, equation (4) becomes
`lambda u=0`, so eliminate `u`.  At `v=c!=0`, the fiber is

```text
k[u,w,x]/(
 c^n u^m x+lambda u+rho c^r w+beta(c)+uc H(u,c,w)).   (5)
```

Map this surface to `A1_u`.  Over `u!=0`, eliminate `x`.  Over `u=0`,
the equation is the nonzero affine-linear equation
`rho c^r w+beta(c)=0`, so eliminate `w` and leave `x` free.  The surface
is regular: off `u=0` this is clear after eliminating `x`, while on
`u=0` the `w` derivative is `rho c^r!=0`.  It is equidimensional over
the regular curve `A1_u`, hence flat by miracle flatness.  All geometric
fibers are smooth affine lines, so it is an `A1`-fibration.  The standard
affine-line fibration theorem, followed by
`Pic(A1)=H^1(A1,O)=0`, makes it the trivial bundle `A2`.

Thus `Spec(B)->A1_v` is an `A2`-fibration.  The characteristic-zero
triviality theorem for affine-plane fibrations over a smooth affine curve
(Sathaye locally over DVRs, then Bass--Connell--Wright) gives

```text
B=k[v]^[2]=k^[3].
```

Since the original hypothesis is the actual splitting `R=B[f]`, a
polynomial basis of `B` together with `f` is a polynomial basis of `R`.
Therefore `f` is a coordinate. QED.

## 4. Why the splitting matters

The normal form (4) contains Vénéreau-type polynomials, so it cannot in
general be rectified merely from its displayed shape by elementary rows.
The conclusion above instead proves first that the quotient is `A3` by
using the full family and then invokes the given equality `R=B[f]`.
Without that equality, `R/(f)=k^[3]` alone would be an
Abhyankar--Sathaye hyperplane statement and would not by itself make `f`
a coordinate.
