# Initial kernels, saturation, and global minimality

Let

\[
R=k[x_1,x_2,x_3,x_4],\qquad D\in\operatorname{LND}_k(R),
\qquad B=\ker D,
\]

and assume that `D` has a slice.  We use the ordinary degree filtration,
write `delta=D_top`, and put

\[
A=\operatorname{in}(B)\subset K:=\ker\delta.
\]

For a least-degree slice `s`, put `h=in(s)`.  When the top coefficient
degree of `D` is positive, the strict degree argument gives

\[
h\in K\setminus A. \tag{1}
\]

This note audits whether global minimality of the coefficient degree under
ambient automorphisms can force a saturation property contradicting (1).

## 1. The initial algebra always has transcendence degree three

The conditional phrase "if `trdeg A=3`" can in fact be removed in the
slice situation.

### Proposition 1.1

For every slice LND on `k^[4]`,

\[
\operatorname{trdeg}_k\operatorname{in}(\ker D)=3.
\]

**Proof.**  Let `L=Frac(R)` and `M=Frac(B)`.  Ordinary degree defines the
discrete valuation

\[
\nu(P/Q)=\deg Q-\deg P
\]

on `L`; its value group is `Z` and its residue field is the function field
of the hyperplane at infinity, of transcendence degree three over `k`.
Restrict `nu` to `M`.  The restricted value group is nonzero (any
nonconstant element of `B` has negative value), hence is a subgroup
`eZ` and still has rational rank one.

Because a slice gives `R=B[s]`, one has `L=M(s)` and
`trdeg_M L=1`.  The Abhyankar inequality for the valued extension
`L/M` gives

\[
\operatorname{trdeg}_{\kappa(M)}\kappa(L)
+\operatorname{rat.rank}(\Gamma_L/\Gamma_M)\leq1.
\]

The quotient of `Z` by `eZ` has rational rank zero.  Since
`trdeg_k kappa(L)=3`, this implies `trdeg_k kappa(M)>=2`.  Applied to
`M/k`, the Abhyankar inequality gives the reverse bound

\[
\operatorname{trdeg}_k\kappa(M)+1\leq
\operatorname{trdeg}_k M=3.
\]

Therefore `trdeg_k kappa(M)=2`.  The associated graded field of `M`
has total fraction field of transcendence degree
`2+rank_Q(eZ)=3`.  Finally, the associated graded field is obtained by
homogeneously localizing `gr(B)`: the initial form of `b/c in M` is the
quotient of the initial forms of `b` and `c`.  Hence its total fraction
field equals `Frac(gr(B))=Frac(A)`, and `trdeg_k A=3`.  QED.

In particular, the element `h` in (1) is always algebraic over
`Frac(A)`, because `A[h] subset K` and the nonzero derivation `delta`
has a three-dimensional kernel.

## 2. Three notions which must not be confused

The following properties are genuinely different.

1. `A` is normal, factorial, or finitely generated as an abstract algebra.
2. `A` is factorially closed in the particular overring `K`: if
   `alpha,beta in K` and `0 != alpha beta in A`, then
   `alpha,beta in A`.
3. When `Frac(A)=Frac(K)` and `A` is a Krull domain, `K` has no poles over
   codimension-one points of `Spec(A)`:

   \[
   K\subseteq A_{\mathfrak p}\quad
   \text{for every }\mathfrak p\in\operatorname{Spec}A,
   \ \operatorname{ht}\mathfrak p=1. \tag{2}
   \]

Property 1 is intrinsic to `A`; properties 2 and 3 concern its embedding in
`K`.  In particular, factoriality does **not** imply factorial closedness in
an overring.

There is also a misleading possible use of the word "saturation":

\[
\{q\in K:\text{there is }0\ne a\in A\text{ with }aq\in A\}.
\]

If `Frac(A)=Frac(K)`, this set is all of `K`, so it supplies no criterion at
all.  The relevant condition is the no-pole condition (2), or factorial
closedness of the embedding.

## 3. Rigorous sufficient criteria

### Proposition 3.1 (codimension-one no-pole criterion)

Suppose that

* `A` is a Krull domain;
* `Frac(A)=Frac(K)`;
* (2) holds.

Then `A=K`.  Consequently no positive-degree slice LND can satisfy these
three conditions.

**Proof.**  A Krull domain is the intersection of its height-one local
rings inside its fraction field:

\[
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}.
\]

Thus (2) gives `K subset A`; the reverse inclusion is part of the
definition of `K`.  If the coefficient degree of `D` were positive, (1)
would contradict `A=K`.  QED.

For a normal noetherian `A`, "Krull" is automatic.  Equivalently, after
the birationality assumption, it is enough to prove that every element of
`K` has nonnegative valuation at every prime divisor of `A`.

### Proposition 3.2 (factorially closed embedding)

Suppose that `Frac(A)=Frac(K)` and that `A` is factorially closed in `K`.
Then `A=K`.

**Proof.**  For `q in K`, write `q=g/p` with `0 != p,g in A`.  The equality
`pq=g in A`, applied in `K`, implies `q in A`.  QED.

Again, this excludes positive coefficient degree by (1).  Notice that the
hypothesis is factorial **closedness**, not that `A` is a UFD.

### Proposition 3.3 (integral birational criterion)

Suppose `A` is normal, `Frac(A)=Frac(K)`, and `K` is integral over `A`.
Then `A=K`, hence the coefficient degree of `D` is zero.

This is just integral closedness in `Frac(A)`.  Neither finiteness nor
integrality can be omitted, as the Anick calculation below shows.  Also,
normality without equality of fraction fields is insufficient: for example
`k[t^2] subset k[t]` has normal source after renaming `t^2` as a variable,
but is a nontrivial integral extension.

### Proposition 3.4 (relative algebraic closedness)

Assume

\[
\{r\in R:r\text{ is algebraic over }\operatorname{Frac}(A)\}=A. \tag{3}
\]

Then the coefficient degree of `D` is zero.

**Proof.**  Since `A[h] subset K` and `K` has transcendence degree at most
three, `h` is algebraic over `Frac(A)`.  Condition (3) gives `h in A`,
contradicting (1) if the coefficient degree is positive.  QED.

Condition (3) holds if `A` itself is the kernel of a derivation of `R` in
characteristic zero.  Indeed, if `A=ker partial` and `r in R` is algebraic
over `Frac(A)`, differentiating its minimal polynomial shows
`partial(r)=0` (separability), hence `r in A`.

These propositions are useful sufficient classes, but none derives its
embedding hypothesis from global minimality.

## 4. Complete audit on the Anick coordinate

Put

\[
\Delta=xw-yz,\quad u=x+z\Delta,\quad v=y+w\Delta,
\]

and

\[
D=(1-zw)\partial_x-w^2\partial_y.
\]

Then `D(u)=1`, `D(v)=D(z)=D(w)=0`, `(u,v,z,w)` is a coordinate
system, and `B=k[v,z,w]`.  The top derivation and its kernel are

\[
\delta=-w(z\partial_x+w\partial_y),\qquad
K=k[z,w,\Delta]. \tag{4}
\]

The weighted-leading-substitution argument (weights `3,1,1` on
`v,z,w`) gives the *whole* initial algebra, not merely the algebra
generated by the leading forms of a casually chosen generating set:

\[
A=\operatorname{in}(B)=k[z,w,w\Delta]. \tag{5}
\]

Writing `t=w Delta`, (4)--(5) become

\[
A=k[z,w,t]\subset K=k[z,w,\Delta],\qquad t=w\Delta. \tag{6}
\]

Thus both `A` and `K` are finitely generated smooth factorial normal
threefold algebras, and

\[
\operatorname{Frac}(A)=\operatorname{Frac}(K).
\]

Nevertheless the inclusion is not saturated.  At the height-one prime
`(w) subset A`,

\[
\Delta=t/w\notin A_{(w)}.
\]

For the least-degree slice `u`,

\[
h=\operatorname{in}(u)=z\Delta=zt/w
\]

also has valuation `-1` at `(w)`.  In particular:

* `A` being normal is insufficient;
* `A` being a UFD is insufficient;
* finite generation of `A` and `K` is insufficient;
* smoothness of both algebras is insufficient;
* birationality `Frac(A)=Frac(K)` together with all the preceding
  properties is still insufficient;
* `K` is not integral over `A`, and `A` is not factorially closed in `K`,
  since `w Delta=t in A` but `Delta notin A`.

Geometrically, (6) is the affine modification

\[
\mathbb A^3_{z,w,\Delta}\longrightarrow\mathbb A^3_{z,w,t},
\qquad t=w\Delta.
\]

Its image omits the open part `w=0, t!=0` of the divisor `w=0`.  Thus the
entire defect is genuinely divisorial, not a codimension-two pathology.

There is no contradiction with *global* minimality: this presentation is
not globally minimal, because the ambient automorphism
`(x,y,z,w) -> (u,v,z,w)` conjugates `D` to `partial_u`.  What the example
does prove is that abstract quality of `A` (even polynomiality) cannot be
the mechanism by which global minimality gives saturation.  Any such
mechanism must detect and eliminate the boundary divisor `(w)` by using
lower-order terms and a companion invariant (`v` here); the graded
inclusion (6) by itself does not construct the conjugating automorphism.

The same pole persists for every least-degree slice.  Such a slice has
the form `u+b(v,z,w)` and degree three.  Its cubic leading form is

\[
z\Delta+c\,w\Delta+p_3(z,w)
=\frac{zt+cwt+wp_3(z,w)}w.
\]

Modulo `w`, the numerator is `zt`, so its valuation at `(w)` is `-1`.
Changing the least-degree slice therefore does not repair the
codimension-one defect for this fixed presentation.

## 5. What global minimality can and cannot currently say

Let `mu(D)` be the minimum of the coefficient degree among all ambient
conjugates of a slice LND `D`.  The following equivalence is elementary
but important:

### Proposition 5.1

For slice LNDs on `k^[4]`, the three-dimensional cancellation statement is
equivalent to

\[
\mu(D)=0\quad\text{for every slice LND }D. \tag{7}
\]

**Proof.**  If cancellation holds, `R=B[s]` and `B isomorphic k^[3]`.
Choose polynomial generators `b_1,b_2,b_3` of `B`.  Then
`(b_1,b_2,b_3,s)` is a coordinate system and `D=partial_s` in these
coordinates, so `mu(D)=0`.

Conversely, if an ambient conjugate has coefficient degree zero, the
standard affine-slice lemma makes it a translation after a linear change
of coordinates.  Its kernel, and hence `B`, is `k^[3]`.  QED.

Consequently, the proposed statement

> a globally coefficient-degree-minimal positive-degree slice LND has
> `h in in(ker D)`

already proves cancellation: it contradicts the strict degree-reduction
lemma.  The stronger statement that `A` is codimension-one saturated in
`K` (together with the birational/Krull hypotheses) does the same by
Proposition 3.1.  Conversely, if cancellation is true, no globally minimal
positive-degree example exists, so such a saturation assertion is
vacuous.  Therefore this is not presently a weaker intermediate lemma;
its essential content is theorem-strength.

Global minimality by definition yields only:

\[
\deg_{\rm coeff}(\Phi D\Phi^{-1})\geq
\deg_{\rm coeff}(D)\quad\text{for every }\Phi\in\operatorname{Aut}(R).
\]

To turn a pole `h=g/p` into a contradiction, one must explicitly build an
ambient automorphism from `p,g` and suitable lower-order data and prove
that it lowers coefficient degree.  The Anick example shows why the
graded fraction alone is insufficient: its successful automorphism needs
both the slice `u` and the companion invariant `v`; neither is recoverable
from the bare inclusion `k[z,w,t] subset k[z,w,Delta]`.

## 6. A genuine pole-elimination lemma in the Anick model

There is one structured situation in which the missing divisor can be
eliminated by an explicit ambient automorphism.  It isolates exactly the
extra lower-order compatibility present in the Anick example.

### Theorem 6.1 (determinantal pole elimination)

Let `R=k[x,y,z,p]`, put

\[
q=xp-yz,
\]

and let `D` be a locally nilpotent derivation satisfying

\[
D(z)=D(p)=0,\qquad D(q)=p. \tag{8}
\]

Then there is a unique `C in R` such that

\[
D(x)=1+zC,\qquad D(y)=pC. \tag{9}
\]

In fact local nilpotence forces

\[
C\in k[z,p,q]. \tag{10}
\]

If `D` has a slice, then `p` divides `C` in `k[z,p,q]`, and `D` is
rectified by one explicit shear.  More precisely, choose

\[
H(z,p,q)=-\int \frac{C(z,p,q)}p\,dq,
\]

where the integral is coefficientwise (characteristic zero), and set

\[
u=x+zH(z,p,q),\qquad v=y+pH(z,p,q). \tag{11}
\]

Then `(u,v,z,p)` is a polynomial coordinate system and

\[
D(u)=1,\qquad D(v)=D(z)=D(p)=0.
\]

**Proof.**  Equation (8) says

\[
pD(x)-zD(y)=p.
\]

Since `p` and `z` are coprime, `p` divides `D(y)`; writing
`D(y)=pC` gives (9), and uniqueness is clear.

We first prove (10), which is not an extra hypothesis.  Pass to
`F=k(z,p)` and divide the extended derivation by the invariant `p`.
On

\[
R_F=F[q,y]
\]

the resulting LND `partial=D/p` has the slice `q` and satisfies
`partial(y)=C`.  The slice decomposition gives

\[
F[q,y]=(\ker\partial)[q],\qquad
\ker\partial\simeq F[q,y]/(q)=F^{[1]}.
\]

Choose a generator `v` of the kernel.  Then
`F[q,y]=F[q,v]`.  An automorphism of the one-variable polynomial ring
over `F[q]` is affine, so

\[
v=a y+b(q),\qquad a\in F^*,\quad b(q)\in F[q].
\]

The equality `partial(v)=0` yields `C=-b'(q)/a in F[q]`.  Now consider
the elementary LND

\[
E=z\partial_x+p\partial_y.
\]

It kills `F` and `q`, hence kills `C` in the common fraction field.
Since `C in R`, it belongs to

\[
\ker(E|_R)=k[z,p,xp-yz]=k[z,p,q],
\]

as follows.  After localizing at `p`, one has
`R_p=k[z,p,p^{-1},q,y]` and `E=p partial_y`, so an invariant lies in
`k[z,p,p^{-1},q]`.  Write such an invariant in `R` as `G(z,p,q)/p^m`
with `m` minimal.  If `m>0`, reduction of
`p^m f=G(z,p,q)` modulo `p` gives `G(z,0,-zy)=0`.  The substitution
`k[z,q] -> k[z,y]`, `q -> -zy`, is injective, hence `G(z,0,q)=0` and
`p|G`, contradicting minimality.  Thus `m=0`, proving the displayed
kernel and (10).

It remains to prove the nonformal point `p|C`.  The ideal `(p)` is
`D`-stable.  Modulo it, using `q=-yz`, the induced derivation on
`k[x,y,z]` is

\[
\overline D=\bigl(1+zC(z,0,-yz)\bigr)\partial_x. \tag{12}
\]

If `s` is a slice of `D`, its residue is a slice of `bar D`.  Hence the
coefficient in (12) divides `1` in `k[x,y,z]` and is a nonzero constant.
Putting `z=0` shows that this constant is `1`, so

\[
C(z,0,-yz)=0.
\]

The substitution map `k[z,q] -> k[y,z]`, `q -> -yz`, is injective:
after expanding in powers of `q`, the coefficient of each power of `y`
is a nonzero power of `z` times the corresponding coefficient.  Thus
`C(z,0,q)=0`, which is precisely `p|C` in `k[z,p,q]`.

Now `H` in (11) is polynomial and, by (8),

\[
D(H)=pH_q=-C.
\]

Equations (9) immediately give `D(u)=1` and `D(v)=0`.  Finally

\[
up-vz=xp-yz=q.
\]

Therefore (11) has the polynomial inverse

\[
x=u-zH(z,p,up-vz),\qquad
y=v-pH(z,p,up-vz),
\]

and is an ambient automorphism.  QED.

The local slice `q/p` visible away from the divisor `p=0` is therefore
globalized exactly when the reduction on that divisor permits it.  In this
model, the global-slice hypothesis itself supplies the divisibility needed
to remove the pole.

### Corollary 6.2 (strict top-degree lowering)

Keep (8)--(10), and give `z,p` degree one and `q` degree two, as induced
from `R`.  Let `C_N` be the top weighted-homogeneous part of `C`.  If
`p|C_N`, put

\[
H_N=-\int(C_N/p)\,dq
\]

and make the shear `X=x+zH_N`, `Y=y+pH_N`.  Since
`Xp-Yz=q`, in the new coordinates

\[
D(X)=1+z(C-C_N),\qquad D(Y)=p(C-C_N). \tag{13}
\]

Thus, unless `C=C_N` and the action is already rectified, the coefficient
degree drops strictly from `N+1` to at most
`1+deg(C-C_N)<N+1`.  This is an actual automorphism-lowering mechanism,
not merely a lift in an associated graded ring.

For Anick, `p=w`, `q=Delta`, and `C=-p`; hence `H=q`.  Formula (11) is
exactly

\[
(x,y,z,w)\longmapsto(x+z\Delta,y+w\Delta,z,w).
\]

More generally, taking any `P in k[q]` gives

\[
C=-pP'(q),\quad
D=(1-zpP'(q))\partial_x-p^2P'(q)\partial_y,
\]

and the shear with `H=P(q)` rectifies it.  Its initial inclusion has the
same divisorial shape `k[z,p,pq^m] subset k[z,p,q]` when the top term of
`P` is `q^m`; the companion invariant `v=y+pP(q)` is exactly the
lower-order datum which makes pole elimination possible.

The determinantal hypotheses (8) are substantive, although (10) is now a
consequence rather than an extra assumption.  Without two fixed ambient
coordinates and a determinant `q` satisfying `D(q)=p`, there is no reason
for the remaining coefficient to be a function of `(z,p,q)`.  A trial
shear can then replace lower-degree `x,y`-terms by high-degree expressions,
so cancellation of the displayed top form need not lower the true
coefficient degree.  The bare graded data `A subset K` contain no assertion
corresponding to (8).

## 7. Exact usable frontier

For a globally minimal hypothetical positive-degree pair, a rigorous next
step may take either of the following concrete forms.

1. Prove `Frac(A)=Frac(K)` and the no-pole statement (2), divisor by
   divisor.  Normality of `A` then finishes the argument, but normality
   alone does not address the pole statement.
2. Prove directly that `A` is factorially closed in `K`, not merely that
   `A` is factorial.
3. Prove that `K` is integral and birational over normal `A`.
4. Given a negative valuation of `h` at a prime divisor of `A`, construct
   from the corresponding lower-order terms an explicit ambient
   automorphism lowering coefficient degree.  This is the only option on
   which global minimality itself could act, and it is precisely the
   missing mechanism in the general case.

The Anick audit rules out replacing any of these embedding statements by
finite generation, normality, factoriality, smoothness, or birationality
of the initial algebra.  No proof that global minimality supplies the
needed codimension-one condition has been obtained; asserting it without
the explicit automorphism construction would simply repackage the
cancellation conjecture.
