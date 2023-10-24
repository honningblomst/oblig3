import pytest
from leepyear import leapyear

@pytest.fixture()
def leap_year():
    return leapyear


def test_if_leapyear_is_dividable_by_4(leap_year):
    check_year = leap_year(2000)
    assert check_year.isLeapYear() == True

    check_year = leap_year(2400)
    assert check_year.isLeapYear() == True


def test_if_leapyear_is_dividable_by_400(leap_year):
    check_year = leap_year(2000)
    assert check_year.isLeapYear() == True

    check_year = leap_year(1998)
    assert check_year.isLeapYear() == False


def test_if_leapyear_is_not_dividable_by_100(leap_year):
    check_year = leap_year(1900)
    assert check_year.isLeapYear() == False

    check_year = leap_year(1998)
    assert check_year.isLeapYear() == False


def test_if_leepyear_is_dividable_by_4_but_not_100(leap_year):
    check_year = leap_year(2020)
    assert check_year.isLeapYear() == True

    check_year = leap_year(2002)
    assert check_year.isLeapYear() == False
