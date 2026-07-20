# The cubic frontier for slice polynomials

**Update.**  The degree restriction in the elliptic-cone case developed
below has now been removed.  The complete argument is in
`linear_affine_modification_theorem.md`: first a general theorem rectifies
every cancellation polynomial `f=u x+G(y)` with `u` a coordinate, and then
a height argument reduces every cubic with leading form a cone over a
smooth plane cubic to that theorem.  The older bounded-degree proof is
retained here because its homogeneous-LND calculations remain useful for
auditing other approaches.

Let `k` be algebraically closed of characteristic zero and
`R=k[x_1,...,x_m]`.  Write a cubic polynomial as

```
f=f_3+f_2+f_1+f_0
```

with homogeneous pieces.  If `R=B[f]`, then the derivation
`D=partial/partial f` satisfies `D(f)=1`; hence the gradient ideal
`(f_{x_1},...,f_{x_m})` is the unit ideal.

## 0. A necessary condition at infinity

The projective hypersurface `f_3=0` in `P^(m-1)` must be singular.  In
fact, homogenize the `m` first partial derivatives to quadrics in
`P^m` with coordinates `[x_1:...:x_m:t]`:

```
H_i = partial_i(f_3)+t partial_i(f_2)+t^2 partial_i(f_1).
```

If `f_3=0` were smooth, the `H_i` would have no common point on `t=0`.
But `m` positive-degree homogeneous polynomials in `m+1` variables have
a common projective zero: otherwise their ideal would have height
`m+1`, contrary to Krull's height theorem.  Such a common zero would
therefore have `t!=0`, and dehomogenizing it would give a common zero of
the affine gradient of `f`, a contradiction.  (Euler's identity ensures
that a projective common zero of the partials of `f_3` lies on `f_3=0`.)

This is only a necessary condition; Section 3 below shows that the
singular locus can be as small as one point even for a coordinate.

## 1. A genuine cubic class: essential rank one at infinity

**Proposition.**  Suppose `deg(f)=3`, the gradient of `f` has no common
zero, and

```
f_3=a L^3,              a in k*, L a nonzero linear form.
```

Then there is a constant vector field `partial_v` such that
`partial_v(f) in k*`.  In particular, `f` is a coordinate.  Consequently
the cancellation assertion holds whenever `R=B[f]` and the cubic part
of `f` is a cube of a linear form.

**Proof.**  After a linear change put `L=x`, and write the other variables
as a column `y=(y_1,...,y_n)^t`, where `n=m-1`.  Since `char(k)!=2`, there
are `A,alpha in k`, columns `b,beta in k^n`, and a symmetric matrix
`C in M_n(k)` such that

```
f = a x^3 + (A/2)x^2 + x b^t y + (1/2)y^t C y
             + alpha x + beta^t y + f_0.
```

Thus

```
Q := grad_y(f) = b x + C y + beta,
p := partial_x(f) = 3a x^2 + A x + b^t y + alpha.
```

Let `S` be the affine solution set `Q=0`.

If `S` is empty, inconsistency of this affine linear system gives
constants `lambda_i in k` with

```
sum_i lambda_i Q_i = 1.
```

Therefore the constant vector field
`v=sum_i lambda_i partial_{y_i}` has `v(f)=1`.

Equivalently, this certificate can be read directly from the coefficients:
there is a column `lambda in k^n` such that

```
lambda^t C=0,   lambda^t b=0,   lambda^t beta!=0,
```

and then `(sum_i lambda_i partial_{y_i})(f)=lambda^t beta`.  Thus the proof also
gives a finite linear-algebra algorithm for finding the coordinate
direction.

Suppose that `S` is nonempty.  Its direction space is

```
K = { (xi,eta) in k times k^n : b xi + C eta=0 }.
```

The linear map `[b C]:k^(n+1)->k^n` has a nonzero kernel, so `S` has
positive dimension.  Since the full gradient has no common zero, `p`
has no zero on `S`.  The only nowhere-zero regular functions on an
affine space are constants, so `p|_S` is a nonzero constant.

For `(xi,eta) in K`, restriction to a line in `S` shows that the
coefficient of `t^2` in `p(x+t xi,y+t eta)` is `3a xi^2`.  Hence
`xi=0` for every element of `K`.  Equivalently,

```
b notin im(C),
```

because `b in im(C)` would give an element `(1,eta) in K`.  On the other
hand, every `eta in ker(C)` gives `(0,eta) in K`.  Constancy of `p|_S`
then yields `b^t eta=0` for all `eta in ker(C)`.  Symmetry of `C` gives

```
b in (ker C)^perp = im(C),
```

a contradiction.  Thus `S` must be empty, and the first case applies.

Finally choose linear coordinates `(z,u_2,...,u_m)` in which
`partial_v=partial_z`.  After scaling `z`, the equality
`partial_z f=1` says `f=z+g(u_2,...,u_m)`.  Hence
`(f,u_2,...,u_m)` is a polynomial coordinate system.  QED.

The hypothesis is directly checkable from `f_3`: it says that the cubic
form has one essential variable (equivalently, after scalar extension,
all its first partial derivatives span the one-dimensional space
`k L^2`).  It is sufficient, not necessary.

## 2. A cubic slice need not expose a constant affine direction

In `k[x,y,z,w]` put

```
u=x+y^2,
h=z^3+w^3,
F=y+zu+h=y+zx+zy^2+z^3+w^3.
```

Then

```
k[x,y,z,w]=k[u,F,z,w],
y=F-zu-h,
x=u-(F-zu-h)^2.
```

Thus `F` is a cubic coordinate and

```
D=-2y partial_x+partial_y
```

is an LND with `D(F)=1` and kernel `k[u,z,w]`.  Nevertheless no constant
vector field has a nonzero constant derivative on `F`.  Indeed, for
`v=a partial_x+e partial_y+c partial_z+d partial_w`,

```
v(F)=az+e(1+2zy)+c(x+y^2+3z^2)+3d w^2.
```

If this is constant, comparison of the coefficients of `x`, `w^2`,
`zy`, and `z` gives `c=d=e=a=0`.  Therefore a proposed lemma
asserting that every cubic slice must have a constant translation
direction in the original affine structure is false, even for `m=4`.

## 3. The cubic part can be irreducible with an isolated singularity

The same example from Section 2 has cubic part

```
H=zy^2+z^3+w^3.
```

The plane cubic in `[y:z:w]` is smooth: its partials are

```
2zy,   y^2+3z^2,   3w^2,
```

and have no common projective zero.  It is therefore irreducible,
since two components of a reducible plane cubic meet and make the cubic
singular.  The projective cubic surface `H=0` in `P^3_[x:y:z:w]` is the
cone over this smooth cubic and has singular locus exactly the vertex
`[1:0:0:0]`.  Thus one and the same cubic slice can have irreducible
leading form, isolated singular locus at infinity, and no nonzero
constant directional derivative.  Neither of those three stronger
properties is necessary for a cubic slice to be a coordinate.

## 4. Smooth irreducible cubic fibres still do not replace the slice

Put

```
G=x+x^2y+z^2 in k[x,y,z,w].
```

Its gradient is unimodular, explicitly

```
(1-2xy)G_x+4y^2 G_y=1.
```

Every fibre `G=c` is smooth.  It is also irreducible: as a polynomial in
`y`, it is the primitive linear polynomial

```
x^2 y+(x+z^2-c),
```

and `gcd(x^2,x+z^2-c)=1` in `k[x,z]`.

Nevertheless `G` is not a coordinate.  For the zero fibre set

```
A=k[x,y,z]/(x^2y+x+z^2).
```

It is smooth and hence normal.  Localizing at `x` gives
`A_x=k[x,x^(-1),z]`, a UFD.  The only height-one prime above `x` is
`P=(x,z)`, and `A/(x)=k[y,z]/(z^2)` shows

```
div_A(x)=2P.
```

Nagata's theorem therefore says that `Cl(A)` is generated by `[P]` and
that `2[P]=0`.  The class `[P]` is nonzero: if `P=(g)`, then `g` is a
unit in `A_x`, hence `g=lambda x^r`; but its valuation at `P` would be
`2r`, not `1`.  Thus `Cl(A)=Z/2`.  Polynomial extension preserves the
class group of a normal domain, so

```
Cl(A[w])=Z/2.
```

The zero fibre in `A^4` is consequently not `A^3`, and `G` is not a
coordinate.  This gives a strict counterexample to replacing the slice
hypothesis by the conjunction "unimodular gradient + all fibres smooth
and geometrically irreducible".

The missing isotriviality is visible.  For `c!=0`, choose `alpha^2=c`.
The two primes over `x` are

```
P_+=(x,z-alpha),   P_-=(x,z+alpha),
```

and `div(x)=P_++P_-`.  Nagata's exact sequence, together with
`A_{c,x}^*=k^* x^Z`, gives

```
Cl(k[x,y,z]/(x^2y+x+z^2-c)) = Z.
```

Thus the zero and nonzero fibres are not isomorphic.  A genuine slice
would translate all fibres into one another via `exp(cD)`; this example
pinpoints why smoothness and irreducibility alone are weaker.

## 5. Exact degree equations for a slice derivation

Write a polynomial derivation in standard homogeneous pieces

```
D=D_0+D_1+...+D_d,
```

where the coefficients of `D_r` are homogeneous of degree `r` (so
`D_r` raises ordinary degree by `r-1`).  If `D` is locally nilpotent,
then its top part `delta=D_d` is locally nilpotent as well.  Indeed, on
the associated graded ring, the leading form of `D^N(g)` is
`delta^N(in(g))` whenever the latter is nonzero; local nilpotence of
`D` therefore forces local nilpotence of `delta` on every homogeneous
element.

For a cubic `f=f_3+f_2+f_1+f_0`, the equation `D(f)=1` is exactly the
finite triangular system

```
sum_(r+j-1=q) D_r(f_j) = 0       (q>0),
D_0(f_1) = 1.                    (q=0)
```

Here terms with indices outside `0<=r<=d`, `0<=j<=3` are omitted.
In particular its top three equations are

```
D_d(f_3)=0,
D_d(f_2)+D_(d-1)(f_3)=0,
D_d(f_1)+D_(d-1)(f_2)+D_(d-2)(f_3)=0.
```

Thus the only unconditional top-degree conclusion is that `f_3` is
invariant under a homogeneous LND.  The examples in the next section
show that neither the degree nor the existence of a slice for this top
LND can be added to that conclusion.

There is nevertheless a clean positive endpoint at degree one.

**Lemma (affine slice fields).**  Let `R=k[x_1,...,x_m]` and let
`D=(Mx+c) dot grad` be an affine-coefficient LND.  If `D(f)=1` for some
`f`, then `ker(D)=k^[m-1]` and `f` is a coordinate.

**Proof.**  Local nilpotence on the finite-dimensional space of affine
linear polynomials implies that `M` is nilpotent.  If `c` belonged to
`im(M)`, an affine translation would give a point `a` with `Ma+c=0`.
Then `D(g)(a)=0` for every polynomial `g`, contradicting `D(f)=1`.
Thus `c notin im(M)`.  Linear algebra gives a row vector `lambda` with
`lambda M=0` and `lambda c=1`; the linear coordinate
`ell=lambda x` satisfies `D(ell)=1`.

Put `A=ker(D)`.  The slice theorem gives `R=A[f]=A[ell]`, since
`f-ell in A`.  Reducing the latter equality modulo the linear
coordinate `ell` gives

```
A = R/(ell) = k^[m-1].
```

Consequently `R=A[f]` is a polynomial coordinate presentation.  QED.

## 6. Anick's cubic: the minimal slice degree can be two

In `k[x,y,z,w]` set

```
Delta=xw-yz,
u=x+z Delta,
v=y+w Delta.
```

Then

```
uw-vz=Delta,
x=u-z(uw-vz),
y=v-w(uw-vz),
```

so `(u,v,z,w)` is a polynomial coordinate system.  In particular the
cubic

```
f=u=x+xzw-yz^2
```

is a coordinate.  Transporting `partial_u` to the original coordinates
gives the quadratic-coefficient LND

```
D=(1-zw) partial_x-w^2 partial_y,
D(f)=1.
```

This degree cannot be lowered even if local nilpotence is dropped:
there is no affine-coefficient derivation `E` with `E(f)=1`.  To see
this, write

```
E=A partial_x+B partial_y+C partial_z+G partial_w
```

with affine-linear `A,B,C,G`, and put `H=xzw-yz^2`.  Comparing degrees
in `E(x+H)=1`, the linear and constant terms first force

```
A=1,
```

while the quadratic part forces `E_0(H)=0`, where `E_0` is the constant
part of `E`.  If the constant terms of `(A,B,C,G)` are `(1,b,c,g)`, then

```
E_0(H)=zw-bz^2+c(xw-2yz)+g xz.
```

The coefficient of `zw` is `1`, a contradiction.  Hence the minimal
coefficient degree among all derivations sending `f` to `1` is exactly
two.

The cubic part `H=z(xw-yz)` has a positive-dimensional projective
singular locus.  Indeed its four partial derivatives are

```
zw, -z^2, xw-2yz, xz,
```

and their common zero set in `P^3` is

```
{z=0, xw=0},
```

the union of the two projective lines `{x=z=0}` and `{z=w=0}`.
Thus even positive-dimensional singular locus at infinity does not
force an affine slice field.

There is also no bound on the degree of an arbitrarily chosen slice
LND, even with this one fixed cubic `f`.  In coordinates `(u,v,z,w)`,
for every `N>=1` put

```
D_N=partial_u+u^N partial_v.
```

This is locally nilpotent, has `D_N(u)=1`, and in the original
coordinates is

```
D_N(x)=1-zw+u^N z^2,
D_N(y)=-w^2+u^N(1+zw),
D_N(z)=D_N(w)=0.
```

Its coefficient degree is `3N+2`; its top homogeneous component is

```
delta_N=H^N z (z partial_x+w partial_y).
```

Since `z partial_x+w partial_y` kills both `z,w` and
`Delta=xw-yz`, the multiplier `H^N z` lies in its kernel, so
`delta_N` is indeed an LND and `delta_N(H)=0`.  All its coefficients
have the common factor `H^N z`, hence it has no slice.  This gives
explicit counterexamples to both proposed degree-filtration lemmas:

1. the leading homogeneous part of a slice LND need not itself have a
   slice;
2. its degree cannot be bounded in terms of the degree of the cubic
   slice polynomial.

The distinction between an arbitrary slice field and one of *minimal*
coefficient degree is essential: for this `f` the minimum is two, not
zero or one.

## 7. Low-degree leading fields over an elliptic cubic cone

The irreducible-cone example of Section 3 admits a useful partial
classification which is stronger than the bare equation
`delta(f_3)=0`.

**Proposition.**  Let `H in k[y_1,y_2,y_3]` define a smooth plane cubic,
and work in `k[x,y_1,y_2,y_3]`.  Suppose `delta` is a homogeneous LND
whose coefficients have common degree `d=1` or `d=2`, and
`delta(H)=0`.  Then

```
delta=q(y_1,y_2,y_3) partial_x
```

for a homogeneous form `q` of degree `d`.

**Proof.**  Put `H_i=partial H/partial y_i`.  Smoothness of the
projective cubic says that `(H_1,H_2,H_3)` has affine zero set only the
origin.  It therefore has height three and is a regular sequence in
`k[y_1,y_2,y_3]`, and remains one after adjoining `x`.  Exactness of
its Koszul complex says that every relation

```
a_1 H_1+a_2 H_2+a_3 H_3=0
```

is generated by the Koszul relations.  In particular there is no such
relation with all `a_i` homogeneous of degree one, while every relation
with all `a_i` homogeneous of degree two has the form

```
(a_1,a_2,a_3)^t=A grad(H)
```

for a constant skew-symmetric matrix `A`.  (This also shows directly
that no powers of `x` occur in the `a_i`.)

For `d=1` it follows at once that `delta(y_i)=0`.  For `d=2`, the
restriction of `delta` to `k[y_1,y_2,y_3]` is the LND

```
theta=(A grad(H)) dot grad_y.
```

We claim that `A=0`.  If not, a nonzero vector `c` spans the kernel of
the three-by-three skew matrix `A`, so the linear form `ell=c dot y`
and the cubic `H` are algebraically independent elements of
`ker(theta)`.  A nonzero LND on a three-dimensional polynomial ring
makes the generic curve of the map

```
(H,ell): A^3 -> A^2
```

rational: after passing to the fraction field of its kernel, the slice
theorem identifies the ambient function field with a one-variable
rational function field.

But that generic curve has genus one.  After making `ell` one of the
linear coordinates, its projective closure is

```
H(Y_1,Y_2,ell*T)-h T^3=0.
```

For generic `(h,ell)` it is smooth: affine singularities are excluded
outside the proper discriminant locus, and at `T=0` smoothness follows
from smoothness of the original projective cubic (the `T` derivative
contains `ell H_3`, with generic `ell!=0`).  It is therefore a smooth
plane cubic, contradicting rationality.  Hence `A=0` and again
`delta(y_i)=0`.

Finally write `delta(x)=a(x,y)`.  Since all `y_i` are fixed, this is an
LND of `k(y)[x]`.  In characteristic zero, `a(x,y) partial_x` is locally
nilpotent only when `a` is independent of `x` (compare `x`-degrees in
its iterates).  Homogeneity gives `a=q(y)` of degree `d`, as asserted.
QED.

Consequently, if a cubic slice has leading form equal to a cone over a
smooth plane cubic and its slice derivation has coefficient degree at
most two, then its top homogeneous field is necessarily a vertical
translation with an invariant homogeneous multiplier.  Section 3 is
the degree-one instance.  The remaining coefficient equations in
Section 5, rather than the top equation alone, are indispensable for
deciding whether a degree-two field can be lowered.

In dimension four those lower equations and local nilpotence do in fact
settle the degree-two case.

**Theorem (elliptic cone, slice degree at most two).**  Let
`R=k[x,y_1,y_2,y_3]`, let `f` be cubic with top form
`f_3=H(y_1,y_2,y_3)`, where `H=0` is a smooth plane cubic, and suppose
there is an LND `D` of coefficient degree at most two with `D(f)=1`.
Then `ker(D)=k^[3]` and `f` is a coordinate.

**Proof.**  Degree zero or one is covered by the affine-slice lemma.
Suppose the coefficient degree is two.  The proposition gives

```
D_2=q(y) partial_x,                 q!=0, deg(q)=2.
```

Write the relevant part of `D_1` and the quadratic part of `f` as

```
D_1(x)=a x+ell(y),
D_1(y)=x c+M y,
f_2=(a_2/2)x^2+x ell_2(y)+Q_2(y).
```

(The scalar called `a_2` is unrelated to `a`.)  The degree-three
coefficient equation `D_2(f_2)+D_1(H)=0` gives, from its terms divisible
by `x`,

```
a_2 q + partial_c(H)=0.             (*)
```

We next use local nilpotence, not just this coefficient equation.  Give
`x` weight three and every `y_i` weight two.  The highest weighted part
of `D` is

```
Gamma=q(y) partial_x+x partial_c,
```

so `Gamma` is an LND.  If `c!=0`, take a linear coordinate `s` in the
`c` direction and regard the other two `y` coordinates as elements of
a coefficient field `K`.  The restriction becomes

```
q(s) partial_x+x partial_s
```

on `K[x,s]`.  Local nilpotence forces `partial_s(q)=0`.  One quick
proof is that

```
x^2-2 integral(q(s) ds)
```

is invariant.  If `q` has positive `s`-degree, its generic level curve
is either a two-place affine conic (`deg_s q=1`) or a genus-one curve
(`deg_s q=2`), whereas the generic orbit quotient of a nonzero LND on
`K^[2]` has affine-line generic fibre.  Thus

```
partial_c(q)=0.                     (**)
```

If `a_2=0`, equation (*) says `partial_c(H)=0`; then `H` is independent
of the direction `c`, making `[c]` a singular point of the projective
cubic.  If `a_2!=0`, (*) and (**) give `partial_c^2(H)=0`.  In
coordinates `(s,r_1,r_2)` this writes

```
H=s A_2(r_1,r_2)+A_3(r_1,r_2),
```

which again makes `[1:0:0]` singular.  Smoothness of `H=0` therefore
forces `c=0`; equation (*) then forces `a_2=0`.

It follows that `D` stabilizes the polynomial subring `k[y_1,y_2,y_3]`,
and its restriction there is the affine LND

```
E=(M y+b) dot grad_y,
```

where `b` is the constant `y`-part of `D`.  Choose a nonzero row vector
`lambda` with `lambda M=0`, which exists because `M` is nilpotent.  If
`lambda b!=0`, the ambient linear coordinate `lambda y` is a slice for
`D`; subtracting a scalar multiple of `f` makes it invariant, and
reduction modulo this ambient coordinate finishes.  If every such `lambda`
annihilates `b`, any one of them gives an ambient invariant linear
coordinate.  Then `D` has rank at most three on `k^[4]`; the established
rank-at-most-three slice theorem (via the resulting `A^2`-fibration
over `A^1`) gives `ker(D)=k^[3]`.  In either case `f` is a coordinate.
QED.

This theorem covers, in particular, the irreducible isolated-singularity
leading form of Section 3 for every slice action of coefficient degree
at most two.  An action of higher minimal coefficient degree remains a
genuine open branch; Section 6 shows why one cannot bound the degree of
a non-minimal choice of slice action.
