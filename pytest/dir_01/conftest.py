#conftest called by pytest for each test in the pytest directory

def pytest_runtest_setup(item):
    print ("setting up", item)