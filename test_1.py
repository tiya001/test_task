import pytest
from task import (get_request, get_ip_address, get_phone_number,
                  validate_phone_number, change_phone_number)

url = "http://sstmk.ru/"
host_name = "sstmk.ru"


def test_status_code():
    assert get_request(url) == 200


def test_ip_address():
    assert get_ip_address(host_name) == '95.142.39.206'


def test_phone_from_site():
    assert get_phone_number(url) == '8 (495) 255-03-39'


@pytest.mark.parametrize(
        "number, result",
        [
            ("+7(495)222-22-22", True),
            ("(495)222-22-22", True),
            ("(34111)2-22-22", True),
            ("+123(456)789-01-23", True),
            ("123-45-67", False),
            ("8 (495) 255-03-39", False),
            ("aboba", False),
        ]
        )
def test_validate_phone_number(number, result):
    assert validate_phone_number(number) == result


def test_change_number():
    assert change_phone_number("8 (495) 255-03-39") == '+7(495)255-03-39'
