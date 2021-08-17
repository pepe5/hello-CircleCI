# https://docs.pytest.org/en/6.2.x/getting-started.html
def func(x):
    return x + 1

# @pytest.mark.xfail
def test_answer():
    assert func(3) == 4
