# A non-invariant extension class that always collapses to a slice

Keep

```
P=k[a,b,c,d],
D(a)=0, D(b)=a, D(c)=b,
p=b^2-2ac, q=p-1, D(d)=q.
```

Let `P_0(T) in k[T]` be nonconstant and define on `P[v]`

```
E=D+P_0(c) partial_v.
```

Then `E` has a polynomial slice.  The same holds if `E(v)` is replaced
by `P_0(c)+D(g)` for any `g in P`, by the shear `v -> v-g`.

## Computation in the cokernel

First consider `delta=a partial_b+b partial_c` on `k[a,b,c]`.  The
polynomial `p=b^2-2ac` is invariant.  For `j>=1`,

```
delta(c b^(2j-1))
 = ((2j+1)/2)b^(2j)-((2j-1)/2)p b^(2j-2).
```

Therefore, modulo `delta(k[a,b,c])`,

```
[b^(2j)] = p^j/(2j+1).                       (1)
```

Write `P_0(c)=lambda_m c^m+...+lambda_0`, with `lambda_m!=0`.
Multiplying `E(v)=P_0(c)` by the invariant `2^m a^m` and using
`2ac=b^2-p` gives

```
2^m a^m E(v)
 = sum_(j=0)^m lambda_j 2^(m-j) a^(m-j)(b^2-p)^j.       (2)
```

For `j<m`, formula (1) reduces the corresponding summand modulo the
image of `E` to a scalar multiple of `a^(m-j)p^j`.  This is itself in
the image, because `E(b)=a` and its remaining coefficient is invariant.

For `j=m`, formulas (1) and the binomial theorem reduce the summand to

```
lambda_m kappa_m p^m,
kappa_m=sum_(i=0)^m binom(m,i)(-1)^(m-i)/(2i+1).
```

The scalar is nonzero in characteristic zero, since

```
kappa_m=integral_0^1 (t^2-1)^m dt !=0.
```

More explicitly,

```
kappa_m=(-1)^m 2^(2m)(m!)^2/(2m+1)!.
```

Equation (2) is itself in `E(P[v])`; hence the preceding reductions
prove

```
p^m in E(P[v]).                                (3)
```

Choose `G` with `E(G)=p^m`.  Since `E(d)=p-1` and

```
p^m-(p-1)(1+p+...+p^(m-1))=1,
```

the polynomial

```
S=G-(1+p+...+p^(m-1))d
```

satisfies `E(S)=1`.

For every `P_0` of degree `m`, the construction can be chosen so that
the coefficient of `v` in `S` is a nonzero scalar times `a^m`, while

```
S mod a = b^(2m-1)c+F(b)-(1+b^2+...+b^(2m-2))d
```

up to multiplication by nonzero scalars.  To see the shape, choose the
primitive `G` in (3) by the reductions used above.  Its `v`-coefficient
is a scalar times `a^m`; modulo `a`, the equation `E(G)=p^m` becomes
`b partial_c(G mod a)=b^(2m)`, whence
`G mod a=b^(2m-1)c+F(b)`.  The coefficient of `d` in `S` reduces to the
displayed geometric sum.

Put `A=b^(2m-1)` and `Q=1+b^2+...+b^(2m-2)`.  The identity

```
A*b + Q*(1-b^2)=1
```

shows explicitly that the coefficient row `(A,-Q)` completes to the
matrix

```
[[A,             -Q],
 [1-b^2,           b]]
```

in `SL_2(k[b])`.  Thus this linear change in `(c,d)`, followed by a
translation by `F(b)`, makes the specialization a coordinate in
`k[b,c,d]`.  Maubach's coordinate criterion (Theorem 1.1 in
[Dutta--Lahiri, *On Residual and Stable Coordinates*](https://arxiv.org/abs/1908.03549))
for a polynomial `alpha(a)v+Q(a,b,c,d)` now
applies: if every root specialization of `alpha` is a coordinate, the
whole polynomial is a coordinate.  Here `alpha` is a scalar multiple
of `a^m`, with the sole root `a=0`.  Consequently `S` is an ambient
coordinate and `ker E=k^[4]` for every nonconstant `P_0(c)`.

For example, when `P_0(c)=c^2`, one explicit slice is

```
-d-b^2d+b^3c+2acd-(7/2)abc^2+(15/2)a^2v.
```

Writing `p=b^2-2ac`, this is

```
S=-(p+1)d+b^3c-(7/2)abc^2+(15/2)a^2v.
```

It is linear in `(d,v)` with a coefficient row which is not visibly
unimodular, but the specialization argument above proves that it is a
coordinate nonetheless.  A direct differentiation gives

```
E(S)=1.
```

## A strict extension: affine dependence on `d`

The same conclusion holds for

```
E(v)=P_0(c)+mu*d+D(g),
```

where `P_0` is nonconstant, `mu in k`, and `g in P`.  As before the
last summand is removed by a shear.  For the new `d`-term use the exact
identity

```
D(bd-c(p-1))=a*d.
```

If `m=deg(P_0)>=1`, then

```
a^m*d=D(a^(m-1)(bd-c(p-1))).
```

Thus the additional term in `2^m a^m E(v)` is already in the image of
`E`, and the cokernel calculation still produces `p^m in im(E)` and a
slice of the form

```
S=C a^m v+H(a,b,c,d).
```

Modulo `a`, its `v`-coefficient vanishes and it is a slice for
`b partial_c+(b^2-1)partial_d`.  This last derivation is standard:

```
r=bc-d,                 u=(b^2-1)c-bd
```

give `bar(D)(r)=1`, `bar(D)(u)=0`, and the change `(c,d) -> (r,u)`
has determinant `-1`.  Hence every one of its slices is
`r+Phi(b,u)`, and is a coordinate.  Therefore `S` is a coordinate modulo `a`,
and Maubach's criterion again shows that `S` is an ambient coordinate.
Consequently these affine-in-`d` extensions are proper translation
actions as well.
