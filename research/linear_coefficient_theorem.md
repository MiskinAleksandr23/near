# A linear-coefficient affine-modification theorem

Let `k` be algebraically closed of characteristic zero.  Put

\[
R=k[x,y_1,y_2,y_3]
\]

and suppose that `R=B[f]` with `f` transcendental over `B`.  This note
proves a direct cancellation class which is useful for cubic polynomials.

## 1. The general theorem

**Theorem.**  Suppose

\[
f=u x+G(y_1,y_2,y_3),
\]

where `u` is a coordinate of `k[y_1,y_2,y_3]`.  Then `f` is a
coordinate of `R`, and `B isomorphic k^[3]`.

After an automorphism of the `y`-space we may and do write `u=y_1`.
Set

\[
g_0(y_2,y_3)=G(0,y_2,y_3),\qquad
X=\operatorname {Spec}(R/(f)).
\]

The stable presentation supplies four facts used below:

1. `X` is smooth, because `B[f]=R` is regular and regularity descends
   from a polynomial extension;
2. `B` is a UFD, since `B` is normal and
   `Cl(B)=Cl(B[f])=Cl(R)=0`;
3. `B^*=k^*`, by comparison of units in `B[f]=R`;
4. `chi_c(X)=1`, since `X times A1 isomorphic A4` and compactly
   supported Euler characteristic is multiplicative.

The cases in which `g_0` is constant are immediate.  If `g_0=0`, then
`G=y_1K` and `f=y_1(x+K)` is reducible, contradicting that
`R/(f)=B` is a domain.  If `g_0=c in k^*`, the shear `x'=x+(G-c)/y_1`
gives `f=y_1x'+c`, and hence

\[
B\simeq k[y_1,y_1^{-1},y_2,y_3],
\]

contrary to `B^*=k^*`.  Thus `g_0` is nonconstant and its zero set

\[
C=V(g_0)\subset A^2_{y_2,y_3}
\]

is nonempty.

### Smoothness and irreducibility of the center curve

The curve `C` is smooth.  Indeed, at a singular point `(alpha,beta)` of
`C`, the point

\[
y_1=0,\quad (y_2,y_3)=(\alpha,\beta),\quad
x=-G_{y_1}(0,\alpha,\beta)
\]

would annihilate all four partial derivatives of
`f=y_1x+G`, contradicting smoothness of `X`.

It is also irreducible.  Write the squarefree factorization
`g_0=c p_1...p_r`; squarefreeness follows from smoothness.  Each

\[
P_i=(y_1,p_i)\subset B
\]

is a height-one prime, because
`B/P_i=k[x,y_2,y_3]/(p_i)` is a domain.  If `r>=2`, factoriality of
`B` makes `P_i=(h_i)` for an irreducible `h_i`.  But

\[
B_{y_1}=k[y_1,y_1^{-1},y_2,y_3]
\]

and `P_iB_{y_1}` is the unit ideal.  Hence `h_i` is a unit in this
localization, so `h_i=lambda y_1^m` in the common fraction field for
some `lambda in k^*` and `m in Z`.  On the other hand,

\[
\operatorname {div}_B(y_1)=P_1+\cdots+P_r,
\]

where every multiplicity is one, while
`div_B(h_i)=P_i`.  These two divisor equalities are incompatible for
`r>=2`.  Therefore `r=1` and `C` is irreducible.

### Euler characteristic and rectification

Decompose `X` according to `y_1`.  On the principal open `y_1!=0`, the
equation uniquely eliminates `x`, and on the closed divisor `y_1=0` it
leaves `x` free.  Thus

\[
X_{y_1}\simeq G_m\times A^2,\qquad
V_X(y_1)\simeq A^1\times C.
\]

Additivity and multiplicativity of `chi_c`, together with
`chi_c(G_m)=0`, give

\[
1=\chi_c(X)=\chi_c(C).
\]

For a smooth irreducible affine curve over an algebraically closed field,

\[
\chi_c(C)=2-2g-r_\infty,
\]

where `g` is the genus of its smooth projective completion and
`r_infty>=1` is the number of missing points.  Equality with one forces
`g=0` and `r_infty=1`; hence `C isomorphic A1`.

The Abhyankar--Moh--Suzuki theorem now rectifies the closed embedding
`C subset A2`.  After an automorphism of `k[y_2,y_3]` and a scalar
rescaling, we may assume

\[
g_0=y_2.
\]

Consequently `G=y_2+y_1K(y_1,y_2,y_3)`.  The two triangular
automorphisms

\[
x'=x+K(y_1,y_2,y_3),\qquad y_2'=y_2+y_1x'
\]

send `f` to the ambient coordinate `y_2'`.  This proves the theorem.

The use of exponent one in `ux` is essential only after the divisor step.
For `u^m x+G`, `m>=2`, the same UFD/valuation argument still forces
`G|_(u=0)` to be nonconstant, irreducible, and squarefree.  What fails is
that the derivative in the `u` direction no longer lets one choose `x` to
detect singularities of the center curve, and higher normal terms are not
removed by the final shear.  The Koras--Russell equations lie precisely
beyond this boundary.

## 2. Cubics whose leading form is an elliptic cone

**Corollary.**  Suppose `deg f=3` and, after a linear change,

\[
f_3=H(y_1,y_2,y_3),
\]

where `H=0` is a smooth plane cubic.  If `R=B[f]`, then `f` is a
coordinate.  No restriction on the degree of a slice LND is needed.

Because the cubic part contains no `x`, the polynomial has the form

\[
f=A x^2+xL(y)+G(y),
\]

where `A in k`, `L` is affine linear, and the leading cubic part of `G`
is `H`.

If `A!=0`, complete the square by the affine change

\[
x'=x+L(y)/(2A),\qquad f=A(x')^2+G_1(y),
\]

where `(G_1)_3=H`.  The three homogenized partial derivatives of `G_1`
are positive-degree forms in four homogeneous variables.  By the height
theorem they have a common projective zero.  Such a zero cannot lie on
the hyperplane at infinity, because there the equations are
`H_{y_1}=H_{y_2}=H_{y_3}=0`, which have no common projective zero by
smoothness of the plane cubic.  Hence `G_1` has an affine critical point;
together with `x'=0` this is a critical point of `f`, contradicting
`D(f)=1`.  Therefore `A=0`.

If `L=0`, exactly the same height argument gives an affine critical point
of `G=f`, again impossible.  If `L` is a nonzero constant, `f` is
immediately a coordinate.  Otherwise `L` is a coordinate of the affine
three-space in the `y` variables, and the theorem of Section 1 applies to

\[
f=L(y)x+G(y).
\]

Thus all cases are exhausted.  This strictly removes the earlier
assumption that the coefficients of a chosen slice LND have degree at
most two.
