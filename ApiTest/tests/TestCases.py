import pytest

from src.ApiCall import CircleApi


@pytest.fixture
def data():
    pass


def test1():
    #test1:success test
    days = CircleApi.generate_random_days(5)
    start, end = CircleApi.generate_random_time()
    name = CircleApi.generate_random_name()
    response = CircleApi().test_offtime_api(days, start, end, name,0)
    response_json = response.json()
    assert 200 == response.status_code
    assert 'success' in response_json['result']


def test2():
    #test2:invalid day range
    response = CircleApi().test_offtime_api('456789N', '07:30', "08:28", 'school', 'N')
    response_json = response.json()
    assert 500 == response.status_code
    assert 'fail' in response_json['result']
    assert 'add user flex offtime: invalid day range' in response_json['error']


def test3():
    #test3:invalid start time
    response = CircleApi().test_offtime_api('012345N', '9:23', "18:28", 'School','N')
    response_json = response.json()
    assert 500 == response.status_code
    assert 'fail' in response_json['result']
    assert 'add user flex offtime: invalid start time' in response_json['error']


def test4():
    #test4:specified ids must already exist
    response = CircleApi().test_offtime_api('012345N', '9:23', "18:28", 'School','9')
    response_json = response.json()
    assert 500 == response.status_code
    assert 'fail' in response_json['result']
    assert 'add user flex offtime: specified ids must already exist' in response_json['error']


def test5():
    #test5:do not enter id
    response = CircleApi().test_offtime_api('012345N', '09:23', "18:28", 'School','')
    response_json = response.json()
    assert 500 == response.status_code
    assert 'fail' in response_json['result']
    assert 'flexOffTimes: null' in response_json['error']








