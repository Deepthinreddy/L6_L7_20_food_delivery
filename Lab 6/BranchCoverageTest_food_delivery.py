
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# Delivery charge branches

def test_invalid_zero_distance():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_invalid_high_distance():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_free_delivery_branch():
    assert delivery_charge(5, 500, False) == 0


def test_near_distance_branch():
    assert delivery_charge(3, 200, False) == 20


def test_medium_distance_branch():
    assert delivery_charge(8, 200, False) == 40


def test_long_distance_branch():
    assert delivery_charge(10, 200, False) == 60


def test_rain_branch():
    assert delivery_charge(2, 200, True) == 50


# Coupon branches

def test_none_coupon_branch():
    assert apply_coupon(300, None, False) == 300


def test_invalid_coupon_branch():
    with pytest.raises(ValueError):
        apply_coupon(300, "INVALID", True)


def test_welcome_non_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_valid_first_order_welcome():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_below_minimum_order():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_valid_save50_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


# Estimated time branches

def test_no_peak_no_busy():
    assert estimated_time(5, False, False) == 35


def test_peak_not_busy():
    assert estimated_time(5, True, False) == 45


def test_busy_not_peak():
    assert estimated_time(5, False, True) == 50


def test_peak_and_busy():
    assert estimated_time(5, True, True) == 65
