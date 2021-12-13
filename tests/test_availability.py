#test_availability.py
"""A series of tests to ensure the quality of the availability.py API"""

import pytest
import requests


def test_request(flask_port):
    flask_port = 5000       #setting flask_port to an open port

    response = requests.get(f"http://127.0.0.1:{flask_port}/?year=2021&month=12&day=10")       #localhost manually set to address
    try:
        print(response.ok)
        assert response.ok == True

    except:
        raise Exception("not a working day")

    assert dict(workingDay=True) == response.json()


@pytest.mark.xfail       #indicates that test is expected to fail
def test_invalid_day(flask_port):
    flask_port = 5000
    response = requests.get(f"http://127.0.0.1:{flask_port}/?year=2021&month=12&day=A")
    try:
        print(response.ok)
        assert response == 400

    except:
        raise Exception("not a working day")

    assert dict(workingDay=True) == response.json()
