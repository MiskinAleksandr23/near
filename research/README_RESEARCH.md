# Передача исследования: Zariski cancellation, characteristic 0

Мы исследуем задачу из `problem.md`: из

```text
k[x_1,...,x_(n+1)] = B[f]
```

нужно вывести `B=k^[n]`. Основной рабочий случай — `n=3`, то есть
slice-LND на `k^[4]`. Полного доказательства общей гипотезы пока нет.

## С чего начать

1. `proof_search.md` — главный синтез: эквивалентности, реестр подходов,
   доказанные классы, контрпримерные фабрики и точные оставшиеся gaps.
2. Тематические `.md` содержат полные вычисления и adversarial audits.
3. Не переносить частичную редукцию в статус общей теоремы без отдельной
   проверки области применимости.

## Самые сильные результаты текущего раунда

- Полностью закрыт класс
  `f=a(u)x+G(u,v,w)` для любого ненулевого `a(u)`.
- Полностью закрыт класс
  `f=u^m v^n x+G(u,v,w)` для всех `m,n>=1`.
- Более общо закрыт rectangular coefficient
  `f=a(u)b(v)x+G(u,v,w)` с любыми кратностями корней и любой смесью
  constant/nonconstant grid nodes.
- Для общего rational SNC coefficient divisor доказана orientation lemma;
  оставшаяся проблема — глобальная polynomial ruling для произвольно
  вложенных active components.
- Homogeneous rank-three quasi-translation frontier исключён для степеней
  `<=5`; возможный hard пример этого специального типа имеет степень
  `>=6`.
- Несколько естественных char-0 counterexample factories строго исключены
  через class group, boundary divisor matrices или nonaffine quotient.

## Главные незакрытые направления

- Общий full-rank slice-LND на `k^[4]` вне quasi-translation классов.
- Initial-kernel saturation: Anick показывает произвольно большие
  divisorial poles, поэтому normal/UFD/birational аргументы недостаточны.
- Нелинейная proper torsor-фабрика: exact Čech equation известна, но
  arbitrary-degree no-slice theorem ещё не доказан.
- Общие (не rectangular) rational SNC affine modifications.
- Отрицательная ветвь: double Koras--Russell-подобные четырёхмерные
  кандидаты пока не имеют ни polynomial-cylinder construction, ни
  окончательного stable obstruction.

## Полезные файлы

- `univariate_coefficient_theorem.md`
- `monomial_coefficient_theorem.md`
- `snc_constant_nodes.md`
- `homogeneous_rank3_boundary.md`
- `initial_kernel_saturation.md`
- `nonlinear_slice_audit.md`
- `double_kr_candidate.md`
- `counterexample_round2.md`

Работа остановлена на чистой checkpoint-точке 2026-07-20. Следующий агент
может продолжать с реестра в `proof_search.md`, сохраняя параллельно
утвердительную и контрпримерную ветви.
