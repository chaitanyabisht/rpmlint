import rpm
from rpmlint import Pkg


def test_parse_deps():
    for (arg, exp) in (
        ("a, b < 1.0 c = 5:2.0-3 d",
         [("a", 0, (None, None, None)),
          ("b", rpm.RPMSENSE_LESS, (None, "1.0", None)),
          ("c", rpm.RPMSENSE_EQUAL, ("5", "2.0", "3")),
          ("d", 0, (None, None, None))]),
    ):
        assert Pkg.parse_deps(arg) == exp


def test_rangeCompare():
    for (req, prov) in (
        (("foo", rpm.RPMSENSE_LESS, (None, "1.0", None)),
         ("foo", rpm.RPMSENSE_EQUAL, ("1", "0.5", None))),
    ):
        assert not Pkg.rangeCompare(req, prov)


def test_b2s():
    for thing in ("foo", ["foo"], None, []):
        assert thing == Pkg.b2s(thing)
    assert "foo" == Pkg.b2s(b"foo")
    assert ["foo"] == Pkg.b2s([b"foo"])