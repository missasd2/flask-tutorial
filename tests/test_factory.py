from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

"""
函数的参数为 client；
test_hello 函数，会根据参数名，匹配被pytest.fixture装饰器装饰的名为client的函数；
当匹配到函数后，会调用该函数，并将函数的返回值 传递回 test_function。
"""
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
