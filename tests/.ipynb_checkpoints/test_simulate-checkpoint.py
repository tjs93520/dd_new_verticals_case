from simulate import run_scenario

def test_improvement():
    base = run_scenario(runs=1000)
    better = run_scenario(runs=1000, clat_boost=0.02)
    assert better["on_time_rate"] > base["on_time_rate"]
