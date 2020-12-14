from day13.extended_gcd import extended_gcd, solve_congruence, solve_congruences


def test_some_simple():
    a = 7
    b = 19

    gcd, (m, n) = extended_gcd(a, b)

    assert 1 == gcd
    assert 1 == a * m + b * n

    print(m, n)
    # Now test my understanding:
    t = a * (m + b)
    assert t > 0
    assert t < a * b
    assert 0 == t % a
    assert 1 == t % b


def test_solve_congruence():
    a1, n1 = 3, 7
    a2, n2 = 4, 19

    t = solve_congruence(a1, n1, a2, n2)

    assert a1 == t % n1
    assert a2 == t % n2


def test_solve_congruences_base_case():
    a1, n1 = 3, 7
    a2, n2 = 4, 19

    t = solve_congruences([(a1, n1), (a2, n2)])

    assert a1 == t % n1
    assert a2 == t % n2


def test_solve_system_of_congruences():
    congruences = [(3, 7), (4, 19), (10, 31)]

    t = solve_congruences(congruences)

    for a, n in congruences:
        assert a == t % n


def test_puzzle_case():
    congruences = [(0, 7), (-1, 13), (-4, 59), (-6, 31), (-7, 19)]
    t = solve_congruences(congruences)
    # t = 1068781

    for a, n in congruences:
        assert a % n == t % n

    assert 1068781 == t