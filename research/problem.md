Current task statement
Гипотеза Зариского о сокращении в характеристике 0

## Гипотеза Зарисского о сокращении в терминах многочленов

Пусть (k) — алгебраически замкнутое поле характеристики (0), и пусть

[
R = k[x_1,\ldots,x_{n+1}].
]

Предположим, что существуют многочлен

[
f \in R
]

и конечно порождённая (k)-подалгебра

[
B \subseteq R
]

такие, что естественное отображение

[
B[T] \longrightarrow R,
\qquad
T \longmapsto f,
]

является изоморфизмом. Иными словами,

[
R = B[f],
]

причём (f) алгебраически независим над (B).

Тогда гипотеза Зарисского утверждает, что

[
B \cong_k k[y_1,\ldots,y_n].
]

То есть из разложения кольца многочленов от (n+1) переменной в виде

[
k[x_1,\ldots,x_{n+1}]
\cong
B[T]
]

должно следовать, что сама алгебра (B) является кольцом многочленов от (n) переменных.

Поскольку

[
B \cong B[T]/(T),
]

после выбранного изоморфизма также получаем

[
B \cong
k[x_1,\ldots,x_{n+1}]/(f).
]

Поэтому гипотезу можно частично переформулировать так:

> Если кольцо (k[x_1,\ldots,x_{n+1}]) допускает представление
>
> [
> k[x_1,\ldots,x_{n+1}] = B[f]
> ]
>
> как кольцо многочленов от элемента (f) над некоторой (k)-алгеброй (B), то гиперповерхность
>
> [
> f(x_1,\ldots,x_{n+1})=0
> ]
>
> должна быть изоморфна аффинному пространству
>
> [
> \mathbb A^n_k.
> ]

Действительно, её координатное кольцо равно

[
k[x_1,\ldots,x_{n+1}]/(f)
\cong B.
]



Use multiagent v2 aggressively and dynamically. You have up to 10 concurrent agents
available. Do not use a fixed assignment such as “N agents for strategy X.” Instead, manage
the search using the following heuristics:

- Do not tell most agents the currently favored approach. Preserve independence during early
rounds so that agents do not all converge to the same attractive but incomplete reduction.
- Maintain an explicit registry of approach families. Group agents by the mathematical idea
they are using, not by superficial wording. If many agents converge to one family, redirect
some of them toward underexplored formulations.
- Do not allow one approach to dominate merely because it gives elegant reductions. A route
that ends at a lemma equivalent in strength to the original conjecture is not close to
completion unless it supplies a genuinely new proof of that lemma.
- When an approach stalls at a theorem-strength missing lemma, mark that route as blocked.
Only continue assigning agents to it if someone proposes a materially new mechanism,
invariant, or construction.
- Keep several incompatible proof routes alive through multiple rounds. Cross-pollinate
ideas only after independent agents have developed them far enough to expose their real
strengths and gaps.
- Require agents to return concrete lemmas, constructions, equations, or counterexamples to
proposed sublemmas. Reject status reports, vague optimism, and claims that an unproved
global compatibility statement is “routine.”
- The root agent should repeatedly synthesize, challenge, redirect, and launch new rounds.
Do not stop after the first wave fails. Produce a complete proof if one survives audit;
otherwise report only the strongest rigorously proved derivation and its exact remaining
gap.
Do not return merely because current approaches fail or agents report theorem-strength gaps.
Continue launching new rounds, reopening blocked approaches only when there is a genuinely
new mechanism, and searching for fresh formulations.
Return only when a complete affirmative proof has been found and survives adversarial audit.
Do not return a reduction, partial result, isolated missing lemma, “best effort” summary, or
explanation of why the problem is difficult.
Spend at least 8 hours on this before even thinking of returning or giving up.
Public search may be used only for ordinary mathematical background or standard named
theorems, not to search for a solution to this exact conjecture or benchmark. Do not search
the public web merely to determine whether it is open, and do not answer that it is open.