from diamond import diamond


def test_a_diamond():
    assert diamond("A") == ["A"]


def test_b_diamond():
    assert diamond("B") == [" A ",
                            "B B",
                            " A "]


def test_c_diamond():
    assert diamond("C") == ["  A  ",
                            " B B ",
                            "C   C",
                            " B B ",
                            "  A  "]


def test_d_diamond():
    assert diamond("D") == ["   A   ",
                            "  B B  ",
                            " C   C ",
                            "D     D",
                            " C   C ",
                            "  B B  ",
                            "   A   "]
