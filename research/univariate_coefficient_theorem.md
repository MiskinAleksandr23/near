# Cancellation for a coefficient depending on one variable

Let `k` be algebraically closed of characteristic zero and put

```
R=k[x,u,v,w].
```

## Theorem

Suppose

```
f=a(u)x+G(u,v,w),       0!=a(u) in k[u],
R=B[f].
```

Then `f` is a coordinate of `R` and `B=k^[3]`.

The conclusion includes arbitrary multiplicities among the roots of `a`.
No smoothness assumption on the plane curves cut out by the specializations
of `G` is needed.

## 1. Every parallel hypersurface has the stable properties

For every `c in k`, evaluation at the polynomial variable `f` gives

```
B_c:=R/(f-c) = B.
```

Consequently every `B_c` is a smooth factorial domain with unit group
`k^*`, and

```
chi_c(Spec(B_c))=1.
```

Here regularity and the class group descend from
`B[f]=R`, units are unchanged under a polynomial extension, and compactly
supported `ell`-adic Euler characteristic gives the last equality from
`B x A1=A4`.

If `a` is constant, `partial_x(f)=a in k^*` and the theorem is immediate.
Assume henceforth that

```
a=lambda product_(i=1)^r (u-alpha_i)^(m_i),
```

where the `alpha_i` are distinct, `m_i>=1`, and `r>=1`.  Set

```
g_i(v,w)=G(alpha_i,v,w).
```

For later use, `k[u]` injects into every `B_c`: if a nonzero polynomial in
`u` belonged to `(f-c)`, comparison of degrees in `x` in the polynomial
domain `R` would be impossible.

## 2. Divisor lemma for all translates

**Lemma.**  For every `i` and every `c in k`, the polynomial `g_i-c` is
nonconstant, irreducible, and squarefree.

**Proof.**  First exclude the degenerate cases.  If `g_i-c=0`, then both
`a(u)x` and `G-c` are divisible by `u-alpha_i`, so `f-c` is reducible.  This
contradicts that `B_c=R/(f-c)` is a domain.  If `g_i-c` is a nonzero
constant, then the equation of `B_c` shows that the divisor `u=alpha_i` is
empty, so `u-alpha_i` is a unit of `B_c`; this contradicts
`B_c^*=k^*` together with the just-noted injection of `k[u]`.  Thus
`g_i-c` is nonconstant.

Factor

```
g_i-c=d product_(j=1)^s p_j^(e_j)
```

with the `p_j` distinct and irreducible.  For every `j`, the ideal

```
P_j=(u-alpha_i,p_j) subset B_c
```

is a height-one prime, since

```
B_c/P_j=k[x,v,w]/(p_j).
```

As `B_c` is regular, `(B_c)_(P_j)` is a DVR.  Reduction modulo
`u-alpha_i` gives

```
B_c/(u-alpha_i)=k[x,v,w]/(g_i-c),
```

and localization at the generic point of `p_j` therefore yields

```
ord_(P_j)(u-alpha_i)
 =length((B_c)_(P_j)/(u-alpha_i))=e_j.              (1)
```

Notice that the multiplicity `m_i` of `alpha_i` as a root of `a` does not
occur in (1).  The calculation concerns the Cartier divisor of
`u-alpha_i`, whose scheme-theoretic quotient is displayed above.

Factoriality gives `P_j=(h_j)` for a prime element `h_j`.  After inverting
`a`, the equation eliminates `x` and gives

```
(B_c)_a=k[u,a^(-1),v,w].
```

Its unit group is

```
k^* product_(ell=1)^r (u-alpha_ell)^Z.
```

Since `h_j` becomes a unit there, in the common fraction field

```
h_j=d_j product_ell (u-alpha_ell)^(n_ell),
      d_j in k^*, n_ell in Z.                       (2)
```

Take valuations of (2) at all height-one primes above `u-alpha_i`.
The divisor of the left side is exactly `P_j`, while (1) gives

```
delta_(j,j')=n_i e_(j')       for every j'.         (3)
```

At primes above any other root, (2) also forces the corresponding
`n_ell` to vanish, but this is not needed.  Equation (3) is impossible if
`s>1`; if `s=1`, it says `1=n_i e_1`, hence `e_1=1`.  Thus `g_i-c` is
irreducible and squarefree.  QED.

## 3. Euler characteristic forces a generic coordinate line

Fix `c`.  On the open subset `a(u)!=0` of `Spec(B_c)`, eliminate `x`:

```
D(a)= (A1_u \ {alpha_1,...,alpha_r}) x A2_(v,w).
```

The complement is the disjoint union of the `r` closed strata

```
u=alpha_i:   A1_x x V(g_i-c).
```

Additivity and multiplicativity of compactly supported Euler
characteristic give

```
1=chi_c(B_c)=1-r+sum_i chi_c(V(g_i-c)),
```

or

```
sum_i chi_c(V(g_i-c))=r                         (4)
```

for every `c`.

Each map `g_i:A2->A1` is dominant.  By generic smoothness in characteristic
zero, there is a nonempty open subset of `A1` over which all the finitely
many maps `g_i` are smooth.  Choose `c` in their common smooth locus.  The
divisor lemma says that every curve `V(g_i-c)` is irreducible.  If its smooth
projective completion has genus `q_i` and `s_i>=1` points at infinity, then

```
chi_c(V(g_i-c))=2-2q_i-s_i <=1.
```

Equality (4), a sum of `r` integers each at most one, forces equality for
every `i`.  Hence `q_i=0`, `s_i=1`, and

```
V(g_i-c)=A1.
```

The Abhyankar--Moh--Suzuki theorem rectifies this embedded affine line in
`A2_(v,w)`.  Therefore `g_i-c`, and hence `g_i`, is a coordinate of
`k[v,w]` for every root `alpha_i` of `a`.

## 4. The quotient is an affine-plane fibration

Return to `B=B_0` and regard it as a finitely presented `k[u]`-algebra:

```
B=k[u,x,v,w]/(a(u)x+G(u,v,w)).
```

The inclusion `k[u]->B` is injective (equivalently, compare `x`-degrees in
the prime ideal `(f)`), and `B` is a domain.  Thus `B` is torsion-free, hence
flat, over the PID `k[u]`.

Every fiber is an affine plane.  If `a(beta)!=0`, eliminate `x`.  If
`beta=alpha_i`, then

```
B/(u-alpha_i)=k[x,v,w]/(g_i),
```

which is `k^[2]` because `g_i` is a plane coordinate.  The same descriptions
hold over the generic point and after residue-field extension.  Hence
`Spec(B)->A1_u` is an `A2`-fibration in the scheme-theoretic sense.

The characteristic-zero triviality theorem for affine-plane fibrations over
a smooth curve now gives

```
B=k[u]^[2].
```

One precise algebraic route is: Sathaye trivializes the fibration over every
rank-one DVR containing `Q`; finite presentation spreads these local
isomorphisms; Bass--Connell--Wright identifies the resulting locally
polynomial algebra with the symmetric algebra of a rank-two projective
`k[u]`-module; and that module is free because `k[u]` is a PID.

Finally `R=B[f]` turns a `k[u]`-polynomial basis of `B`, together with `f`,
into four polynomial generators of `R`.  Thus `f` is an ambient coordinate
and `B=k^[3]`.  QED.

## 5. Consequence for the cusp frontier

Taking `a(u)=u^m` shows that no singular rational-unibranch special center
can occur in a cancellation datum of this form.  Indeed the all-level UFD
argument, applied to `f-c` for generic `c`, forces `G(0,v,w)-c` to be a
coordinate line and therefore forces `G(0,v,w)` itself to be a coordinate.
This eliminates the entire Russell/Koras--Russell univariate-coefficient
mechanism, not only cusps with particular Puiseux pairs.
