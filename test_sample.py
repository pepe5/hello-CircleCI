# https://docs.pytest.org/en/6.2.x/getting-started.html
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
