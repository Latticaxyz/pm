def test_smoke_import_top_level():
    __import__("pm")


def test_smoke_import_public_api():
    from pm import polymarket

    assert polymarket is not None
