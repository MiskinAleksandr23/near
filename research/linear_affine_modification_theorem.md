# A linear affine-modification cancellation theorem

Let `k` be algebraically closed of characteristic zero. This note isolates a
class of hypersurfaces for which the cancellation datum itself forces the
defining polynomial to be a coordinate.

## 1. The theorem

**Theorem.** Put

```
R=k[x,y_1,y_2,y_3]
```

and suppose

```
f=y_1 x+G(y_1,y_2,y_3).
```

If there is a `k`-algebra `B` such that `R=B[f]`, then `f` is a coordinate of
`R`. Equivalently, `B isomorphic to k^[3]`.

The same statement holds with `y_1` replaced by any coordinate of
`k[y_1,y_2,y_3]`.

**Proof.** Evaluation at `f=0` identifies

```
B = R/(f)
  = k[x,y_1,y_2,y_3]/(y_1x+G).
```

Moreover `B^[1]=R=k^[4]`. We will use the following immediate consequences:

```
B is a smooth factorial domain,       B^*=k^*.
```

Indeed regularity and factoriality descend from a polynomial extension, and
the units of `B` equal the units of `B[T]`.

Set

```
g_0(y_2,y_3)=G(0,y_2,y_3),
C=V(g_0) in A^2_(y_2,y_3).
```

First, `g_0` is neither zero nor a nonzero constant. If `g_0=0`, then
`G=y_1K` and

```
f=y_1(x+K),
```

contrary to the fact that `B=R/(f)` is a domain. If `g_0 in k^*`, the relation
`y_1x=-G` shows that the closed set `y_1=0` in `Spec(B)` is empty, so `y_1` is
a unit of `B`; this contradicts `B^*=k^*`.

Next, `C` is smooth. If `p=(a,b)` were a singular point of `C`, then

```
g_0(p)=partial_(y_2)g_0(p)=partial_(y_3)g_0(p)=0.
```

At the point of the hypersurface `Spec(B)` given by

```
y_1=0, (y_2,y_3)=p,
x=-partial_(y_1)G(0,p),
```

all four partial derivatives of `y_1x+G` vanish. This contradicts smoothness
of `B`.

We now show that `C` is irreducible. Smoothness makes `g_0` squarefree; write
its distinct irreducible factors as `p_1,...,p_s`. For each `i`,

```
P_i=(y_1,p_i) subset B
```

is a height-one prime, and

```
div_B(y_1)=P_1+...+P_s.
```

Because `B` is factorial, `P_i=(h_i)` for a prime element `h_i`. On the other
hand, eliminating `x` after inverting `y_1` gives

```
B_(y_1)=k[y_1,y_1^(-1),y_2,y_3],
(B_(y_1))^*=k^* y_1^Z.
```

Thus the image of `h_i` in this localization is `c y_1^n`. Taking valuations
at all the `P_j` gives

```
delta_(ij)=n                 for every j.
```

This is impossible if `s>1`. Therefore `s=1` and `C` is smooth irreducible.

It remains to identify this affine curve. Use compactly supported Euler
characteristic (either singular Euler characteristic after descent and
embedding in `C`, or `ell`-adic Euler characteristic). It is additive and
multiplicative, and `chi_c(A^m)=1`, `chi_c(G_m)=0`. From

```
B times A^1 isomorphic to A^4
```

we get `chi_c(B)=1`. The decomposition by `y_1` is

```
B_(y_1):       D(y_1) isomorphic to G_m times A^2,
B/(y_1):       V(y_1) isomorphic to A^1_x times C.
```

Consequently

```
1=chi_c(B)=0+chi_c(C).
```

If the smooth projective completion of `C` has genus `g` and its complement
has `r` points, then

```
chi_c(C)=2-2g-r.
```

Here `r>=1` because `C` is affine and positive-dimensional. Hence
`2-2g-r=1` forces `g=0`, `r=1`, and `C isomorphic to A^1`.

By the Abhyankar--Moh--Suzuki theorem, the embedding `C subset A^2` is
rectifiable. After an automorphism of `k[y_2,y_3]` and a scalar rescaling we
may therefore assume

```
g_0=y_2.
```

It follows that `G=y_2+y_1K(y_1,y_2,y_3)`. The shear

```
x'=x+K
```

is a polynomial coordinate change and gives

```
f=y_2+y_1x'.
```

Finally `(x',y_1,f,y_3)` is a coordinate system, with inverse
`y_2=f-y_1x'`. Thus `f` is a coordinate. QED.

## 2. Cubics whose leading form is an elliptic cone

**Corollary.** Let

```
f in k[x,y_1,y_2,y_3]
```

have degree three, and suppose its cubic homogeneous part is

```
f_3=H(y_1,y_2,y_3),
```

where `H=0` is a smooth plane cubic. If `R=B[f]`, then `f` is a coordinate
and `B isomorphic to k^[3]`.

**Proof.** Because `R=B[f]`, the derivation `partial/partial f` transported
from `B[f]` gives a polynomial vector field `D` with `D(f)=1`. In particular
the affine gradient of `f` has no common zero.

Since the cubic part has no `x`, write

```
f=A x^2+xL(y_1,y_2,y_3)+G(y_1,y_2,y_3),
```

where `A in k` and `L` is affine linear.

Suppose first that `A!=0`. Completing the square by the affine shear

```
x'=x+L/(2A)
```

gives

```
f=A(x')^2+G'(y),
```

and the cubic part of `G'` is still `H`. The three partial derivatives of
`G'` have a common affine zero. Indeed, homogenize them to three quadrics in
`P^3_[y_1:y_2:y_3:t]`. By Krull's height theorem, three positive-degree
homogeneous polynomials in four variables have a common projective zero. A
common zero on `t=0` would be a common projective zero of
`H_1,H_2,H_3`, impossible because `H=0` is smooth (Euler's identity places a
common zero of the partials on `H=0`). Hence the common zero has `t!=0` and
is affine. Together with `x'=0` it is a common zero of the full gradient of
`f`, a contradiction. Therefore `A=0`.

We now have

```
f=xL(y)+G(y).
```

If `L=0`, the identical homogenized-gradient argument applied to `G` gives a
common zero of the gradient of `f`. If `L` is a nonzero constant, `f` is
immediately a coordinate, since `partial_x(f)=L in k^*`.

The remaining case is that `L` is a nonconstant affine-linear coordinate of
`k[y_1,y_2,y_3]`. An affine change of the `y` variables makes `L=y_1`, so the
theorem applies and proves that `f` is a coordinate. QED.

## 3. Why the exponent one matters

The proof uses essentially that the modification is linear in the divisor
coordinate:

```
f=y_1x+G.
```

For `f=y_1^m x+G` with `m>=2`, the divisor argument actually still forces
`G(0,y_2,y_3)` to be nonconstant, irreducible, and squarefree: if its prime
factors have multiplicities `e_i`, valuations give
`delta_ij=n_i e_j`, hence there is one factor and its multiplicity is one.
What fails is different.  A singular point of the center curve no longer
lets us choose `x` to annihilate `partial_(y_1)f`, and even a rectified smooth
center does not make the final shear linear when higher normal terms remain.
Koras--Russell type hypersurfaces lie precisely beyond this boundary.  Thus
the exponent-one theorem does not extend to `m>=2` by the same reasoning,
although the factorial divisor control survives.

The subsequent adversarial audit proves a genuine extension not reproduced
here: for exponent `m=2`, a smooth special center is sufficient, using an
explicit exponential of a triangular LND in place of the final shear.  It
also treats the terminal jet for every `m`; see
`linear_affine_modification_audit.md`, Section 4.

The audit also gives the strongest conceptual extension.  For every
`m>=1`, if the special plane curve `G(0,y_2,y_3)=0` is smooth, then it is
an embedded `A1` by the divisor/Euler argument and AMS.  The quotient

`k[x,u,v,w]/(u^m x+G)`

is then a flat `A2`-fibration over `A1_u`: nonzero fibers eliminate `x`,
and the zero fiber eliminates the rectified center coordinate `v`.
Sathaye's DVR theorem, local spreading, Bass--Connell--Wright, and
Quillen--Suslin trivialize it as `k[u]^[2]`.  Thus the cancellation
conclusion holds for all `m` with smooth center.  Only singular rational
unibranch centers remain in the higher-m branch.
