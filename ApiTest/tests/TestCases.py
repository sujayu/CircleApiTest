import pytest

from src.ApiCall import CircleApiTestCase

@pytest.fixture
def data():
    pass

def test1():
    #test1:success test HTTP code 200(all values are given correctly)
    response = CircleApiTestCase('012', '01:20', '02:20', 'School', 'N')
    response_json = response.get_call()
    assert 'success' in response_json['result']

def test2():
    response = CircleApiTestCase('0ads2n', '01:20', '02:20', 'School', 'N' )
    response_json = response.get_call()
    assert 'fail' in response_json['result']

def test3():
    response = CircleApiTestCase('012345N', '1:20', '2:20', 'School', 'N' )
    response_json = response.get_call()
    assert 'fail' in response_json['result']

def test4():
    response = CircleApiTestCase('012345N', '1:20', '2:20', 'School', 'N')
    response_json = response.get_call()
    assert 'true' in response_json.ok()