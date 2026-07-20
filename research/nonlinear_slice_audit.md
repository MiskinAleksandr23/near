# Slice audit for the genuinely nonlinear proper family

Throughout,

```text
P=k[a,b,c,d],                 q=b^2-2ac-1,
D(a)=0, D(b)=a, D(c)=b, D(d)=q,
r=ad-qb,
h=q^2c-qbd+ad^2/2,
C=ker D=k[a,q,r,h]/(2ah-r^2+q^2(q+1)),
lambda=h psi(h),              psi != 0,
w=1+lambda d^m,               m>=2,
E=D+w partial_v.
```

The graph argument in `higher_torsor_graph.md` proves that this action
is free and proper.  This note isolates the slice question without
putting any a priori bound on the `v`-degree.  It also proves that no
slice affine-linear in `v` exists.  The last step, excluding arbitrary
`v`-degree, is not completed here.

## 1. Exact two-chart criterion, with arbitrary `v`-degree

On `D(a)` use the old slice `s_a=b/a`; on `D(q)` use
`s_q=d/q`.  Define the corresponding `E`-invariant orbit integrals

```text
u_a = v-s_a-lambda integral (r/a+q s_a)^m ds_a,
u_q = v-s_q-lambda q^m s_q^(m+1)/(m+1).
```

Thus

```text
(ker E)_a=C_a[u_a],       (ker E)_q=C_q[u_q].             (1)
```

The scaled invariants in `higher_torsor_graph.md` are

```text
U_m=a^(m+1)u_a,           V_m=q u_q.
```

The invariant called `J_m` there has a particularly simple closed
form:

```text
J_m=r^(m+1)/(m+1).                                      (2)
```

Indeed `J_m` is in `C`.  After inverting `a`, translate the old
`D`-orbit to the representative `b=0`; then `d=r/a`, and the displayed
formula defining `J_m` reduces to `a^(m+1)d^(m+1)/(m+1)`.  Equality on
the dense open `D(a)` proves (2).  Consequently

```text
u_a-u_q = g,
g = r/(a q) + lambda r^(m+1)/((m+1)a^(m+1)q).            (3)
```

Every local slice on the two charts is respectively

```text
s_a+F_a(u_a),   F_a in C_a[T],
s_q+F_q(u_q),   F_q in C_q[T].                          (4)
```

Since

```text
s_a-s_q=-r/(a q),
```

the two expressions in (4) glue if and only if, on writing `x=u_a`,

```text
F_a(x)-F_q(x-g)=r/(a q).                                (5)
```

This criterion does **not** assume that a putative slice is linear in
`v`: `F_a,F_q` are arbitrary polynomials.

It is also sufficient for a global polynomial slice.  The complement
of `D(a) union D(q)` in `Spec(P[v])` is `V(a,q)`, which has codimension
two (`a=0,q=0` gives `b^2=1`).  A solution of (5) gives a regular
function on that open subset, and normality of the polynomial ring
extends it uniquely across the complement.  The identity `E(S)=1`
then extends as well.  Hence:

> `E` has a polynomial slice if and only if the unrestricted
> polynomial Cech equation (5) has a solution.

For `lambda=0`, take `F_a(x)=F_q(x)=x`; then (3)--(5) recover the slice
`v`.  For the nonlinear family, the residual term

```text
lambda r^(m+1)/((m+1)a^(m+1)q)                          (6)
```

is the precise obstruction that higher powers of `x` would have to
remove.  Thus merely observing that (6) is not a coboundary among
constant functions is not enough: nonlinear `F_a,F_q` could in
principle contribute constant terms through powers of the translation
`g`.

## 2. A full exclusion of slices affine-linear in `v`

Suppose

```text
S=s_0+gamma v,       s_0 in P, gamma in C,
```

and `E(S)=1`.  The coefficient equations are

```text
D(gamma)=0,
D(s_0)=1-gamma(1+lambda d^m).                           (7)
```

After inverting `q`, `P_q=C_q[d/q]`.  Integrating (7) therefore gives

```text
s_0=(1-gamma)d/q-gamma lambda d^(m+1)/((m+1)q)+c,
c in C_q.                                               (8)
```

If `s_0` were polynomial, multiplying (8) by `q` and moving the first
two terms to the other side would produce a polynomial invariant.
Reduction modulo `q` consequently says

```text
-(1-gamma_bar)d
 +gamma_bar h psi(h)d^(m+1)/(m+1)  belongs to C/(q).    (9)
```

Use the standard embedding

```text
C/(q)=k[a,r,h]/(r^2-2ah)  --> k[a,d],
r |-> ad,   h |-> ad^2/2.                               (10)
```

Give a monomial `a^A d^B` the defect `B-2A`.  Every monomial in the
image of (10) has defect at most zero.  Equivalently, write a homogeneous
piece of defect `-j` in `C/(q)` as `gamma_[j]`, with `j>=0`.
Multiplication by `d` raises defect by one, whereas multiplication by

```text
h psi(h)d^(m+1)
```

raises it by `m+1` (the factor in `h` has defect zero).

In the positive-defect components `m+1,m,...,2` of (9), only the
second term can occur.  Since the ring is a domain and `h psi(h)!=0`,
these components force

```text
gamma_[0]=gamma_[1]=...=gamma_[m-1]=0.                 (11)
```

The component of defect one then forces

```text
gamma_[m] h psi(h)d^m/(m+1)=1.                         (12)
```

But the defect `-m` piece of `k[a,r,h]/(r^2-2ah)` is

```text
a^(m/2) k[h]                 if m is even,
r a^((m-1)/2) k[h]           if m is odd.
```

After multiplying by `d^m`, it is contained respectively in

```text
h^(m/2)k[h],    h^((m+1)/2)k[h].                       (13)
```

Thus the left side of (12) is divisible by
`h^(1+ceil(m/2))`, and cannot equal `1`.  This contradiction proves:

> For every `m>=2` and every nonzero `psi`, the proper derivation
> `D+(1+h psi(h)d^m)partial_v` has no slice of `v`-degree at most one.

Notice that this is stronger than the earlier primitive obstruction:
the coefficient `gamma` of `v` was arbitrary, not normalized to one.

## 3. Why the unrestricted step is still substantive

If `S=sum_{i=0}^N s_i v^i`, coefficient comparison gives

```text
D(s_N)=0,
D(s_i)+(i+1)w s_(i+1)=0       (1<=i<N),
D(s_0)+w s_1=1.                                      (14)
```

There is a useful rigorous constraint on the top coefficient.  If
`N>0`, put `gamma=s_N in C`.  The next equation says that `gamma w`
has a primitive in `P`.  Repeating the reduction modulo `q` used in
Section 2 now gives

```text
gamma_bar d+gamma_bar h psi(h)d^(m+1)/(m+1)
    belongs to C/(q).                                  (15)
```

In positive defects `m+1,...,2`, equation (15) successively kills the
defect `0,...,m-1` pieces of `gamma_bar`; in defect one, there is no
standalone `d` term this time, so it also kills the defect `-m` piece.
Consequently

```text
every monomial of gamma_bar has defect at most -(m+1). (16)
```

Thus a nonlinear slice, if it exists, must start with a highly
divisible invariant leading coefficient.  This is an unbounded-degree
constraint, not a bounded search.

For `N>1`, the top equation only says that the invariant multiple
`s_N w` has a primitive.  It forces strong divisibility of `s_N`, but
does not make it zero.  Such divisible leading terms really occur in
global invariants (for example powers and products involving `U_m`
and `V_m`).  Therefore one cannot discard them without proving a
degree-reduction lemma for the full intersection in (1).

Equivalently, in (5), powers of `x-g` contribute constants involving
`g^j`.  A proof that checks only affine `F_a,F_q` is exactly the
forbidden assumption that the slice is linear in `v`.

For orientation only, the sparse modular search in
`slice_linear_search.py` was extended by the test case `1+hd2`; over
`F_1000003` it finds no slice of total degree at most 12.  This is not
used as evidence for the theorem.  The remaining exact problem is the
unbounded polynomial Cech equation (5).
