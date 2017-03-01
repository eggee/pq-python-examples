import pytest

@pytest.fixture(scope="module")
def web(request):
    def fin():
        web_client.client.close()
    if request:
        request.addfinalizer(fin)
    return web_client
