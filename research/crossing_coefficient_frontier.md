# Crossing coefficients: audited theorem and the constant-node frontier

Let

```text
R=k[x,u,v,w],   f=a(u,v)x+G(u,v,w),   R=B[f],
```

over an algebraically closed field of characteristic zero.  For every
`c`, the threefold `X_c=V(f-c)` is isomorphic to `Spec(B)`; hence it is
smooth and factorial, has units `k*`, and has compactly supported Euler
characteristic one.

## 1. Why the naive SNC divisor lemma needs a node correction

Let `a=product p_i^(m_i)` and let `D_i=V(p_i)` be an SNC collection of
embedded affine lines.  On `D_i x A1_w`, write `g_i=G|D_i`.  If
`g_i-c=product q_j^(e_j)`, the primes `(p_i,q_j)` are height one in
`X_c`.  After inverting `a`, their principal generators become units of
`k[u,v,a^-1,w]`, hence monomials in all the `p_l`.

It is **not** always legitimate to keep only the `p_i` valuation.  If
`D_i` meets `D_l` at `s` and the node restriction

```text
h_s(w)=G(s,w)
```

is the constant `c`, then `q_j` can be the local equation of the node
inside `D_i`; the prime `(p_i,q_j)` then also contains `p_l`.  Cross
terms from `ord(p_l)` invalidate the equation
`delta_jj'=n_i e_j'`.

The elementary polynomial

```text
a=uv,   G=u+v(vw+1)
```

shows the issue: at the constant node value zero,
`G(0,v,w)=v(vw+1)` is reducible.  (The associated `f` is nevertheless
a coordinate, since it is linear in `(u,w)` with unimodular coefficient
row `(1+vx,v^2)`.)

## 2. A corrected rational-SNC theorem

**Theorem.** Suppose the reduced divisor `D=V(a)_red` is a connected
SNC union of embedded affine lines, with no triple points, and suppose
every node restriction `h_s(w)` is nonconstant.  Then `f` is a
coordinate and `B=k^[3]`.  Arbitrary multiplicities of the components
in `a` are allowed.

**Proof.** Choose `c` outside all critical values and so that no
`h_s-c` vanishes identically.  At a height-one prime `(p_i,q_j)` above
a factor of `g_i-c`, no other `p_l` is present: otherwise its generic
point would be supported on a node, forcing `h_s-c=0` identically.
The UFD/unit argument is therefore clean at this level and proves that
every `g_i-c` is irreducible and squarefree.

Let the incidence graph have `r` vertices and `e` edges.  Put
`Y_c=V(D,G-c)`.  Stratifying `X_c` over `A2-D` and `D` gives

```text
chi(Y_c)=chi(D)=r-e.                                  (1)
```

Each curve `C_i=V(g_i-c)` is smooth irreducible, so `chi(C_i)<=1`.
At a node `s`, adjacent curves meet in `deg(h_s)>=1` points.  There are
no triple intersections, hence

```text
r-e=sum_i chi(C_i)-sum_s deg(h_s)<=r-e.               (2)
```

Equality forces `chi(C_i)=1` for all `i` and `deg(h_s)=1` for all
nodes.  Thus every `C_i` is `A1`; AMS makes every `g_i` a coordinate of
`k[D_i,w]`.

If a plane coordinate `g(t,w)` restricts at `t=0` to a nonconstant
linear polynomial in `w`, then `(t,g)` is a coordinate pair.  Indeed,
for a companion `q`, the image of `t=0` in the `(g,q)` plane is a graph,
so its ideal is `(q-P(g))=(t)`; hence `k[t,g]=k[t,w]`.  It follows that
`g=alpha w+P(t)`.  Applying this at an incident node of every component
shows that `G(z,w)` is linear with nonzero `w` coefficient for every
`z in D`.

Now `B=k[u,v,x,w]/(ax+G)` over `A2_(u,v)` has fiber `A1_w` off `D`
and fiber `A1_x` on `D`.  Regularity of `B` plus equidimensionality
gives flatness by miracle flatness, and all geometric fibers are smooth.
The standard affine-line fibration theorem makes this a Zariski locally
trivial `Aff_1`-bundle.  Since `Pic(A2)=H^1(A2,O)=0`, it is trivial:
`B=k[u,v]^[1]`.  Finally `R=B[f]` makes `f` a coordinate. QED.

The same conclusion holds for a disconnected SNC collection: disjoint
embedded affine-line graph components in `A2` force all components to be
parallel coordinate lines, reducing to the already audited theorem
`a=a(u)`.

## 3. The reduced crossing `a=uv` is completely closed

Put `g_u(v,w)=G(0,v,w)`, `g_v(u,w)=G(u,0,w)`, and
`h(w)=G(0,0,w)`.  If `h` is nonconstant, the preceding theorem applies
(and also shows directly that `deg h=1`).  Suppose `h=c_0` is constant.
For generic `c!=c_0`, the UFD comparison has no shared node prime, so
both `g_u-c` and `g_v-c` are smooth irreducible curves.  The two curves
are disjoint inside `Y_c`, and (1) becomes

```text
chi(V(g_u-c))+chi(V(g_v-c))=1.                        (3)
```

Both Euler characteristics are at most one.  Therefore their unordered
pair is exactly `(1,0)`: one generic fiber is `A1`, the other is `Gm`.
If, say, the `g_v` fibers are `A1`, AMS makes `g_v` a plane coordinate.
Since its `c_0` fiber contains the whole line `u=0`, irreducibility of a
coordinate fiber forces

```text
g_v-c_0=lambda u,   lambda in k*.                     (4)
```

For the reduced coefficient `a=uv`, (4) permits absorption of every
term of `G-c_0-lambda u-g_u(v,w)` divisible by `uv` into `x`.  Thus the
remaining coordinate question has the exact form

```text
f-c_0=u(lambda+v x)+g(v,w),                            (5)
```

where the generic fiber of `g` is `Gm`, `g(0,w)=0`, and the all-level
factoriality constraints still hold.  The example above corresponds to
`g=v(vw+1)` and is rectified by the unimodular row
`(lambda+vx,v^2)`.

The constant-node branch admits a direct algebraic finish.  Factor

```text
g=v^e product_(j=1)^s p_j^(d_j),                      (6)
```

with no `p_j` associated to `v`.  In the UFD `B_(c_0)`, the height-one
primes over `uv` are `P_0=(u,v)` and `P_j=(u,p_j)`.  Localizing at
`uv` gives the Laurent polynomial ring, whose units modulo `k*` are
generated by `u,v`.  The localization sequence for divisor classes
therefore makes their two divisor vectors generate the free group on
all the `P_j`.  Hence `s<=1`.  The case `s=0` is incompatible with a
generic `Gm` fiber.  For `s=1`, the divisor matrix is

```text
        P_0 P_1
div(u)  e   d_1
div(v)  1   0,
```

so surjectivity over `Z` forces `d_1=1`.  Thus `g=v^e p` with `p`
irreducible.

For every `c!=0`, the curve `V(g-c)` in `Gm_v x A1_w` is smooth:
a singular point would, by choosing the free value of `x`, create a
critical point of `f-c`.  It is irreducible and has Euler characteristic
zero, hence is `Gm`.  The restriction of `v` to it is a nonconstant
unit, thus equals `alpha t^N` in a `Gm` parameter and is etale.  The
ramification criterion for the projection to `v` now gives

```text
V(g_w) intersect (Gm x A1) subset V(g) intersect (Gm x A1).  (7)
```

In the Laurent UFD `k[v^+-1,w]`, the right side is the irreducible
divisor `p=0`.  Any nonunit factor of `g_w` would therefore be associated
to `p`, impossible because `deg_w(g_w)<deg_w(p)`.  The derivative is not
zero (otherwise generic fibers would be unions of affine lines), hence

```text
g=rho v^M w+beta(v),   rho in k*, M>=1.               (8)
```

Equation (5) is affine-linear in `(u,w)`, with coefficient row over
`k[v,x]`

```text
(lambda+vx, rho v^M).
```

which is unimodular: a finite truncation of the geometric series gives
a Bezout identity between `lambda+vx` and any power of `v`.  Complete
this row to `SL_2(k[v,x])`; the resulting linear change of `(u,w)` makes
the linear part one variable, and `beta(v)` is absorbed by a translation.
Hence `f` is a coordinate.

Combining the nonconstant and constant node branches proves:

> If `f=uvx+G(u,v,w)` and `R=B[f]`, then `f` is a coordinate.

For higher powers `u^m v^n`, terms divisible only by `uv` cannot all be
absorbed into the coefficient, so an additional jet problem remains even
after the reduced crossing calculation.
