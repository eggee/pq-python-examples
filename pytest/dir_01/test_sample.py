#usage: python -m pytest test_sample.py --html=/output/results.html  --self-contained-html --junitxml=/output/results.xml
#usage: (set up env vars) - pytest test_sample.py

def func(x):
    return x + 1

def test_answer():
    #expect a failure here
    assert func(4) == 5