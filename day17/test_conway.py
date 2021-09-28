from conway import neighbors


def test_neighbors():
    res = neighbors((0,0,0))

    assert res == {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}
