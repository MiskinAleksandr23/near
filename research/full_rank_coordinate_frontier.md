# A two-parameter Anick family and the minimal-slice frontier

Throughout, let

\[
R=k[x,y,z,w],\qquad \operatorname {char} k=0,
\]

and let `M,N` be positive integers.  Put

\[
\Delta=w^M x-z^M y,
\]

and define

\[
u=x+z^M\Delta^N,\qquad v=y+w^M\Delta^N.
\]

This family is useful as an audit example for any attempt to control a
full-rank slice LND by minimizing the ordinary degree of a slice.  It
generalizes the usual Anick pair (`M=N=1`).

## 1. The coordinate system and its slice field

The equality

\[
w^M u-z^M v=\Delta
\]

shows directly that

\[
(x,y,z,w)\longmapsto(u,v,z,w)
\]

is an automorphism.  Its inverse is

\[
x=u-z^M(w^M u-z^M v)^N,
\qquad
y=v-w^M(w^M u-z^M v)^N.
\]

Let `D=partial_u` in the coordinate system `(u,v,z,w)`.  In the original
coordinates,

\[
D=
\bigl(1-Nz^Mw^M\Delta^{N-1}\bigr)\partial_x
-Nw^{2M}\Delta^{N-1}\partial_y.
\]

Consequently

\[
D(u)=1,qquad \ker D=k[v,z,w].
\]

In particular `D` has rank one, rigorously: the displayed automorphism
conjugates it to a coordinate partial derivative.  Thus this construction
does **not** produce a rank-four candidate.  Its role is to identify which
degree-theoretic phenomena can already occur for a disguised translation.

## 2. Exact minimum of the degree of a slice

Set

\[
L=M+N(M+1).
\]

Both `u` and `v` have ordinary degree `L`.  Every slice of this fixed
derivation has the unique form

\[
s=u+b(v,z,w),\qquad b\in k[v,z,w],
\]

because the difference of two slices belongs to `ker D`.

**Proposition.**  The least ordinary degree of a slice of this fixed `D`
is exactly `L`.

**Proof.**  Give `k[V,z,w]` the weight filtration

\[
\operatorname {wt}(V)=L,\qquad
\operatorname {wt}(z)=\operatorname {wt}(w)=1.
\]

Under the substitution `V -> v`, the highest ordinary form of `V` is
`w^M Delta^N`.  The map

\[
k[V,z,w]\longrightarrow k[x,y,z,w],
\qquad V\longmapsto w^M\Delta^N
\]

is injective: `w^M Delta^N` is transcendental over `k[z,w]` (it has
positive `x`-degree).  It follows that, for every nonzero `b`, the ordinary
degree of `b(v,z,w)` is its weighted degree, and its highest ordinary form
is obtained by the displayed leading substitution.  In particular, there
can be no hidden cancellation between distinct terms of maximum weight.

Suppose `deg(u+b(v,z,w))<L`.  No term of `b` can have weight greater than
`L`, since its nonzero leading substitution would then survive in a degree
where `u` has no term.  The weight-`L` part of `b` has the form

\[
cV+p(z,w),\qquad c\in k,
\]

where `p` is homogeneous of degree `L`.  Cancellation of the degree-`L`
part of `u` would require

\[
z^M\Delta^N+c w^M\Delta^N+p(z,w)=0.
\]

The coefficient of `x^N` in this identity is

\[
(z^M+cw^M)w^{MN},
\]

which is nonzero.  This contradiction proves the lower bound.  The slice
`u` attains it.  QED.

Thus the minimum slice degree for a fixed rank-one slice LND on `k^[4]`
is unbounded.  In this family the coefficient degree of `D` is

\[
N(M+1)+M-1=L-1,
\]

so the exact relation is `min deg(slice)=deg_coeff(D)+1`.

There is a stronger minimality statement which does not assume local
nilpotence and does not keep the derivation fixed.

**Proposition.**  If `N>=2`, the least coefficient degree among all
polynomial derivations `E` of `R` satisfying `E(u)=1` is exactly `L-1`.

**Proof.**  Write

\[
E=A\partial_x+B\partial_y+C\partial_z+G\partial_w.
\]

The four partial derivatives of `u=x+z^M Delta^N` give

\[
\begin{aligned}
u_x&=1+Nz^Mw^M\Delta^{N-1},\\
u_y&=-Nz^{2M}\Delta^{N-1},\\
u_z&=Mz^{M-1}\Delta^{N-1}(\Delta-Nz^My),\\
u_w&=MNz^Mw^{M-1}x\Delta^{N-1}.
\end{aligned}
\]

The equation `E(u)=1` first implies

\[
A-1\in(\Delta^{N-1});
\]

write `A=1+Delta^(N-1) A_1`.  After division by `Delta^(N-1)`, the
same equation becomes

\[
A_1+Nz^Mw^M A-Nz^{2M}B
+Mz^{M-1}(\Delta-Nz^My)C
+MNz^Mw^{M-1}xG=0.                 \tag{*}
\]

Set `x=y=0`.  Since `N>=2`, one has `Delta=0` and `A=1` on this plane.
Equation (*) yields

\[
A_1(0,0,z,w)=-Nz^Mw^M+Nz^{2M}B(0,0,z,w).
\]

The term `-Nz^M w^M` cannot be cancelled by the second summand, which is
divisible by `z^(2M)`.  Hence `deg A_1>=2M`.  Therefore

\[
\deg A\ge (N-1)(M+1)+2M=L-1.
\]

The displayed slice LND `D` has coefficient degree `L-1`, so equality is
attained.  QED.

Thus even for coordinate polynomials in four variables, the degree of a
polynomial vector field certifying `E(f)=1` has no dimension-only bound;
the explicit LND above is already degree-minimal among all certificates.

## 3. Exact initial invariant ring and arbitrary pole order

Let `A=in(ker D)` for the ordinary degree filtration.  The same injective
leading-substitution argument proves the equality

\[
A=k[z,w,w^M\Delta^N].
\]

In particular `A` is a polynomial ring in three variables; it is finitely
generated, normal, and factorial.

The top homogeneous component of `D` is

\[
\delta=-Nw^M\Delta^{N-1}
       (z^M\partial_x+w^M\partial_y).
\]

Multiplication by the nonzero invariant `-Nw^M Delta^(N-1)` does not
change a derivation kernel.  Moreover

\[
\ker(z^M\partial_x+w^M\partial_y)=k[z,w,\Delta].
\]

For completeness, this last equality can be checked after adjoining
`k(z,w)`, where the kernel is `k(z,w)[Delta]`.  If a homogeneous polynomial
in `(x,y)` lies in the intersection with `R`, its coefficient of
`Delta^j` has no denominator: the endpoint coefficients of `Delta^j` are
`w^{Mj}x^j` and `(-z^M)^j y^j`, whose monomial gcd is one.  Separating the
`(x,y)`-degrees gives the assertion term by term.  Hence

\[
\ker\delta=k[z,w,\Delta].
\]

The highest form of the least-degree slice `u` is

\[
h=z^M\Delta^N\in\ker\delta\setminus A.
\]

Its obstruction to lying in `A` is an exact codimension-one pole:

\[
w^M h=z^M(w^M\Delta^N)\in A,
\]

whereas

\[
w^e h\notin A\qquad(0\leq e<M).
\]

Indeed, writing `T=w^M Delta^N`, the embedded polynomial ring is
`A=k[z,w,T]`, and `w^e h=z^M w^{e-M}T`; for `e<M` this has a genuine
negative `w`-valuation in `Frac(A)`.  Thus the required saturation order
is exactly `M`, and is unbounded even among rank-one translations.

There is also a finite extension hidden in the top kernel:

\[
\operatorname {Frac}(A)=k(z,w,\Delta^N)
   \subset k(z,w,\Delta)=\operatorname {Frac}(\ker\delta),
\]

of degree `N` (the indeterminate `Delta` has minimal polynomial
`T^N-Delta^N` over the rational field `k(z,w,Delta^N)`).  The particular
missing element `h` already lies in `Frac(A)`, but has the pole described
above.

## 4. Precise false lemmas and what survives

The family gives strict counterexamples to each of the following proposed
intermediate assertions, even though every `D` here is a translation.

1. A fixed slice LND on `k^[4]` has a slice of degree bounded solely in
   terms of the ambient dimension.
2. For a least-degree slice `s`, finite generation, normality, or
   factoriality of `in(ker D)` forces `in(s)` to belong to `in(ker D)`.
3. There is a dimension-only bound on the power of a boundary equation
   needed to clear the denominator of `in(s)` over `in(ker D)`.
4. The fraction fields of `in(ker D)` and `ker(D_top)` must agree for a
   disguised translation.

What survives is the genuinely stronger saturation criterion: if a
separate argument proves that the highest form of a least-degree slice is
already in `in(ker D)`, its degree can be lowered.  This family shows that
normality of the initial invariant algebra cannot supply that membership,
and that any codimension-one argument must use global minimality under
ambient conjugation or additional geometry, not a uniform pole bound.

The examples do not refute a *globally* minimal presentation: conjugating
by `(x,y,z,w)->(u,v,z,w)` makes `D=partial_u` and the minimum slice degree
one.  They therefore isolate rather than solve the full-rank case.  A
hypothetical rank-four example still has to prevent precisely this kind of
ambient conjugation.

## 5. A direct recognition class for disguised translations

The construction has a useful coordinate-free version over a
two-dimensional coefficient ring.  Let `A=k[z,w]`, choose `a,b in A`, put

\[
\Theta=bx-ay,
\]

and let `P(T) in A[T]`.  Then

\[
U=x+aP(\Theta),\qquad V=y+bP(\Theta)
\]

are coordinates over `A`, because `bU-aV=Theta` and hence the inverse is

\[
x=U-aP(bU-aV),\qquad y=V-bP(bU-aV).
\]

Conjugating `partial_U` back to `(x,y)` gives

\[
\mathcal D=
 (1-abP'(\Theta))\partial_x-b^2P'(\Theta)\partial_y.
\]

Thus any derivation which can be put in the displayed form is visibly a
rank-one slice LND, with coordinate slice `U` and invariant coordinates
`V,z,w`.  Conversely, in characteristic zero every `q(T) in A[T]` has an
antiderivative `P(T)`, so the pattern

\[
(1-abq(\Theta))\partial_x-b^2q(\Theta)\partial_y
\]

is a directly recognizable sufficient tameness class.  No cancellation
or `A^2`-fibration theorem is needed for this conclusion.

The family above is the specialization

\[
a=z^M,\qquad b=w^M,\qquad P(T)=T^N.
\]

This recognition identity is also an audit warning for suspension
constructions: a nonconstant Bezout-looking coefficient can be the
derivative of a shear along an invariant `Theta`, in which case the
apparently complicated slice action is exactly a conjugated translation.

## 6. Classification when both coefficients depend on one linear form

Here is a wider statement which also records exactly where division is
legitimate.  Let `A=k[z,w]`, take relatively prime `a,b in A`, and put

\[
\Theta=bx-ay.
\]

Consider an `A`-derivation

\[
\mathcal E=P(\Theta)\partial_x+Q(\Theta)\partial_y,
\qquad P,Q\in A[T].                         \tag{1}
\]

**Lemma (all LNDs in the one-form ansatz).**  The derivation (1) is
locally nilpotent if and only if

\[
bP(T)-aQ(T)=c\in A.                         \tag{2}
\]

When (2) holds, set `p=P(0)` and `q=Q(0)`.  There is a unique
`r(T) in A[T]` with `r(0)=0` such that

\[
P=p+ar,qquad Q=q+br,qquad c=bp-aq.         \tag{3}
\]

**Proof.**  The restriction of `E` to `A[Theta]` is

\[
(bP(\Theta)-aQ(\Theta))\partial_\Theta.
\]

Over a characteristic-zero domain, `H(T)partial_T` is locally nilpotent
only when `H` has degree zero: if `deg H=1`, its iterates on `T` never
vanish, and if `deg H>1`, their degrees strictly increase.  This proves
necessity.  Conversely, if `E(Theta)=c in A`, then

\[
\mathcal E^n(x)=c^{n-1}P^{(n-1)}(\Theta),\qquad
\mathcal E^n(y)=c^{n-1}Q^{(n-1)}(\Theta)
\]

for `n>=1`, so `E` is locally nilpotent.  Finally, subtracting (2) at
`T=0` gives

\[
b(P-p)=a(Q-q).
\]

Both differences are divisible by `T`, and coprimality of `a,b` in the
UFD `A[T]` gives (3), including uniqueness.  QED.

Formula (3) is not by itself a straightening: writing `r/c` without
checking divisibility is an actual gap.  The exact elementary
straightening criterion is as follows.

**Lemma (shear criterion).**  If `r=c h` for some `h in A[T]`, choose an
antiderivative `H in A[T]` with `H'=-h`.  Then

\[
U=x+aH(\Theta),\qquad V=y+bH(\Theta)
\]

are `A`-coordinates and

\[
\mathcal E(U)=p,qquad \mathcal E(V)=q.
\]

Thus `E` has a slice if and only if `(p,q)=A`, and in that event it is a
rank-one translation.  Explicitly, if `alpha p+beta q=1`, then

\[
S=\alpha U+\beta V,\qquad K=qU-pV
\]

complete `z,w` to a coordinate system, with `E(S)=1` and `E(K)=0`.

The proof is direct: `bU-aV=Theta`, so the shear is invertible, and (3)
together with `E(Theta)=c` gives the two constant derivatives.  For a
constant field `p partial_U+q partial_V`, a slice implies `(p,q)=A` by
evaluating a Bezout identity at `U=V=0`; the converse is the displayed
linear slice.

There is a useful geometric condition under which the slice hypothesis
itself forces the missing divisibility.

**Theorem (squarefree transverse case).**  Assume that `c` is either zero
or a nonunit, that

\[
(a,b,c)=A,
\]

and that `A/(c)` is reduced (for nonzero `c`, this just says that `c` is
squarefree).  If the LND (1) has a slice, then `r in cA[T]`; consequently
the shear criterion applies and `E` is a rank-one translation.

**Proof.**  Put `bar A=A/(c)`.  The images of `a,b` form a unimodular row
over `bar A`.  From `bp=aq` in `bar A`, there is `lambda in bar A` such
that

\[
\bar p=\bar a\lambda,\qquad \bar q=\bar b\lambda.
\]

Indeed, if `alpha a+beta b=1` modulo `c`, take
`lambda=alpha p+beta q` and use the relation.

The constant field

\[
L=\bar a\partial_x+\bar b\partial_y
\]

has a linear slice `ell=alpha x+beta y`, and `(ell,Theta)` are coordinates
over `bar A` (their determinant is `-1`).  Reducing (3) modulo `c` gives

\[
\bar{\mathcal E}
  =(\lambda+\bar r(\Theta))\partial_\ell.
\]

A slice for `E` reduces to a slice for this derivation.  Therefore
`lambda+bar r(Theta)` is a unit of `bar A[ell,Theta]`.  Since `bar A` is
reduced, a unit in its polynomial ring has no nonconstant coefficients.
As `r(0)=0`, it follows that `bar r=0`, i.e. `r in cA[T]`.  The preceding
lemma finishes the proof.  (When `c=0`, the same argument reads `r=0`.)
QED.

If `c` is a unit, divisibility is automatic, and (2) already makes
`(p,q)` unimodular; this is the remaining easy case.

The hypotheses in the theorem are not cosmetic.  Without
`(a,b,c)=A`, the relation `bP=aQ mod c` need not allow one to divide the
pair `(P,Q)` by `(a,b)` in `A/(c)`.  Without reducedness, a nonconstant
polynomial with nilpotent coefficients can be a unit, so reduction of a
slice modulo `c` does not force coefficientwise divisibility by `c`.
The explicit family of Sections 1--3 lies outside the transverse
unimodularity hypothesis (`c=b=w^M`), but is covered by the sharper direct
check `r in cA[T]`.

Finally, the Jacobian of the coefficient pair in (1), with respect to
`x,y`, has rank at most one because both rows are multiples of
`(b,-a)`.  The converse statement requires care: vanishing of
`P_xQ_y-P_yQ_x` only gives algebraic dependence over a fraction field; it
does not produce a common *linear* form over `A`, nor does it justify any
of the divisions by `a`, `b`, or `c` above.  Thus the theorem applies to
the verifiable one-linear-form ansatz, not to a bare Jacobian-rank
condition without an additional polynomial common-generator lemma.

## 7. A broader coordinate-local-slice theorem

The linearity of `Theta` can be dropped if the common polynomial is known
to be an `A`-coordinate.  This gives a second directly checkable tameness
class.

**Theorem.**  Let `R=A[g,l]=k[z,w]^[2]`, and let `E` be an `A`-LND such
that

\[
E(g)=c\in A.
\]

Then necessarily

\[
E=c\partial_g+q(g)\partial_l
\quad\text{for some }q\in A[g].             \tag{4}
\]

If `E` has a slice, then it is a rank-one translation.  No reducedness
assumption on `A/(c)` is needed.  When `A/(c)` is reduced the
straightening is the simple invariant shear from Section 6; in general a
finite nonlinear correction handles the nilpotent coefficients.

**Proof.**  A priori write

\[
E=c\partial_g+Q(g,l)\partial_l.
\]

Let `m=deg_l Q`.  If `m>=2`, the `l`-degree of `E^n(l)` strictly grows:
the top term from `Q partial_l` has nonzero coefficient in the domain
`A[g]`.  If `m=1`, write `Q=a(g)l+b(g)`.  The coefficient of `l` in the
successive iterates is obtained by repeatedly applying

\[
c\frac{d}{dg}+a(g)
\]

starting with `a(g)`.  It never vanishes when `a!=0`: if `deg_g a>0`,
multiplication by `a` gives the unique highest-degree term at every step,
while if `a in A\setminus{0}`, the successive coefficients are powers of
`a`.  This contradicts local nilpotence.  Hence `m=0`, proving (4).

Suppose first that `c` is nonzero and not a unit.  Reducing a slice
equation modulo `c` shows that

\[
\bar q(g)\partial_l
\]

has a slice.  Thus `bar q(g)` is a unit in `(A/(c))[g]`.

Choose `F(g) in A[g]` with `F'=q` and `F(0)=0`.  The polynomial
`bar F` is an automorphism of the affine line over `bar A=A/(c)`.  Indeed,
a polynomial over a ring is a unit precisely when its constant
coefficient is a unit and all its other coefficients are nilpotent.
Therefore `bar q=bar F'` being a unit says that the linear coefficient of
`bar F` is a unit and every higher coefficient is nilpotent (the positive
integers are invertible in `k`).  A linear polynomial plus a nilpotent
polynomial perturbation has a finite compositional inverse.

Put

\[
I=cl-F(g).
\]

Then `E(I)=0`.  Let `bar Psi` be the inverse of the one-variable
automorphism `g -> -bar F(g)`, and lift it to some `Psi in A[T]`.  Since
`I=-F(g) mod c`, the numerator in

\[
s=\frac{g-\Psi(I)}{c}                       \tag{5}
\]

is divisible by `c` in `A[g,l]`.  Thus (5) is a polynomial, and
`E(s)=1`.  More importantly, `(s,I)` are `A`-coordinates.  The inverse is

\[
g=cs+\Psi(I),\qquad
l=\frac{I+F(cs+\Psi(I))}{c}.                \tag{6}
\]

The second numerator is divisible by `c` already in `A[s,I]`, because
modulo `c` the defining inverse identity says
`I+bar F(bar Psi(I))=0`.  Equations (5)--(6) are mutually inverse.
Hence `R=A[s,I]` and `E=partial_s`, proving rank one directly.

If `A/(c)` happens to be reduced, a unit `bar q(g)` is constant.  Then
`q=q_0+ch`, integration and the shear `L=l-H(g)`, `H'=h`, reduce (4) to
the constant field `c partial_g+q_0 partial_L`.  This is the simpler
special case, but not the general mechanism.

If `c` is a unit, divide by `c`, integrate `q/c`, and use `g/c` as a
slice (the companion invariant is `l-integral(q/c)`).  If `c=0`, the
slice equation makes `q(g)` a unit of the reduced polynomial ring
`A[g]`, hence `q in A^*`, and `(l/q,g)` are translation coordinates.
QED.

The nonlinear correction is genuinely needed over a nonreduced
quotient.  For example, take (with `w` passive)

\[
E=z^2\partial_g+(1+zg)\partial_l.
\]

Here `q-1=zg` is not divisible by `c=z^2`, so no shear of the preceding
coefficientwise form can work.  Nevertheless

\[
I=z^2l-g-\frac z2g^2
\]

is invariant and

\[
s=l+\frac{I^2-g^2}{2z}
 =l+\frac{g^3}{2}-zgl+\frac{zg^4}{8}
   -\frac{z^2g^2l}{2}+\frac{z^3l^2}{2}
\]

is polynomial and satisfies `E(s)=1`.  The inverse coordinate formulas
are

\[
g=z^2s-I-\frac z2I^2,
\]

\[
l=s+\frac{I^3}{2}-zsI+\frac{zI^4}{8}
  -\frac{z^2sI^2}{2}+\frac{z^3s^2}{2}.
\]

Thus this is explicitly a rank-one translation, while also being a
counterexample to the claim that a slice forces `q-q(0)` to be divisible
by `c` when `A/(c)` is not reduced.

This result applies after any polynomial `A`-coordinate change `(x,y)` to
`(g,l)`; the distinguished local slice `g` may be highly nonlinear in the
original variables.  It is therefore wider than the one-linear-form
ansatz, while still avoiding the unjustified leap from a rank-one
Jacobian matrix to the existence of a polynomial common coordinate.
