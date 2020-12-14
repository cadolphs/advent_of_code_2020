from typing import Iterable, Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, Tuple[int, int]]:
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 > 0:
        quotient, remainder = divmod(r0, r1)

        r0, r1 = r1, remainder
        s0, s1 = s1, s0 - quotient * s1
        t0, t1 = t1, t0 - quotient * t1

    assert r1 == 0, "Something went very wrong"

    return r0, (s0, t0)


def solve_congruence(a1: int, n1: int, a2: int, n2: int) -> int:
    gcd, (m1, m2) = extended_gcd(n1, n2)
    assert gcd == 1, f"Something went very wrong, numbers {n1, n2} aren't coprime."
    return (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)


def solve_congruences(congruences: Iterable[Tuple[int, int]]) -> int:
    a1, n1 = congruences[0]
    for a2, n2 in congruences[1:]:
        a1 = solve_congruence(a1, n1, a2, n2)
        n1 = n1 * n2
    return a1
