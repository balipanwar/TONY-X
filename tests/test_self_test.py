# test_self_test.py

from tony_x.core.self_test import run_self_test


def test_stage_1_self_test_contract():
    results = run_self_test()
    assert "CORE" in results
    assert results["CORE"]["status"] in {"PASS", "FAIL"}


def test_stage_2_10_self_test_contract():
    from tony_x.core.stage_2_10_self_test import run_stage_2_10_self_test
    results = run_stage_2_10_self_test()
    assert results["CORE"]["status"] == "PASS"
