from main import get_temperature
import requests
import pytest

class MockResponse:
    def __init__(self, resp):
        self.response = resp

    def json(self):
        return self.response

@pytest.mark.parametrize("lat, lng, expect", [(-14.235004, -51.92528, 16)])
def test_get_temperature_by_lat_lng(lat, lng, expect, monkeypatch):
    mockResp = {"currently": {"temperature": 62}}

    def mock_get(*args, **kwargs):
        return MockResponse(mockResp)

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(lat, lng)

    assert result == expect

# invalid lat

test_lat = [
    (None , 17.358746, {"code": 400,
                                "error": "The given location is invalid."}),
    (True, 17.358746, {"code": 400,
                                 "error": "The given location is invalid."}),
    ('11111', 180.358746, {"code": 400,
                                "error": "The given location is invalid."}),
    (9999999 , -180.358746, {"code": 400,
                                 "error": "The given location is invalid."}),
]


@pytest.mark.parametrize("lat, lng, expect", test_lat)
def test_invalid_lat(lat, lng, expect, monkeypatch):
    mockResp = {"currently": {"temperature": 62}}

    def mock_get(*args, **kwargs):
        return MockResponse(mockResp)

    monkeypatch.setattr(requests, "get", mock_get)

    result1 = get_temperature(lat, lng)

    assert result1 == expect

# invalid log
# negative values
# type verification
# key validation
# request response
