# Test Approach
The objective of these tests are to verify the functionality of `availability.py` works according to set specifications

The availability.py API will undergo functional testing, with preloaded data at the time of execution. Unit testing will allow individual aspects of the program to be tested, making it easier to discover issues.
The existing positive test will be fixed, so it can be determined whether the application works as expected. A negative test, i.e. a test that is expected to fail, will test how the application handles out-of-bound values.


## Fixing Failing Test
Upon initally running and inspecting the test_availability.py file, it was discovered that `localhost` is showing a blank screen when accessed in a web browser, and the ports that are assigned to `flask_port` are all closed ports. For the sake of time, `localhost` was changed to 127.0.0.1 and `flask_port = 5000`

It was then identified that the value for day would throw an exception, as this falls on a Saturday. The value for day has been changed to 10 (Friday):

``` python
def test_request(flask_port):
    response = requests.get(f"http://localhost:{flask_port}/?year=2021&month=12&day=10")
```


The final part of the test causing failure was the following line:

```python
assert response.ok == 200
```
Here `response.ok` is equal `True`, yet this line of code is trying to verify that a boolean value is equal to an integer value, which will cause another `AssertionError`. This line should be changed to either:

```python
assert response.ok == True
```

or

```python
assert response == 200
```

where 200 should be the value of response, given that the date input is a working day.

## Adding negative test
Please view test_availability.py for added negative test

### Improvements
Given more time, the following could be refactored into this application:

 1. Allow and test for the handling various different schedules that are more realistic. For example, one carer may only work weekends, whereas another's may change on a weekly basis.

 1. A fix would be implemented to ensure that `localhost` references the correct IP address and that flask_port returns an open port without having to be manually defined.

 1. While the negative test throws an exception as expected, it would be better if the test accounted specifically for the `ValueError` exception and let the user know to enter a valid date. This could possibly be done with the `pytest.raises` function
